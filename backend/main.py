from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
import time
import httpx
from openai import OpenAI
from dotenv import load_dotenv
from csir.context_aggregator import ContextAggregator

load_dotenv()  # MUST come before os.getenv

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # add your deployed domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Rate limit (per IP, per minute) — in-memory stopgap
# ----------------------------
RATE_LIMIT_PER_MIN = int(os.getenv("RATE_LIMIT_PER_MIN", "5"))
_rate = {}  # ip -> (window_start_epoch_seconds, count)

def check_rate_limit(ip: str):
    now = int(time.time())
    window_start, count = _rate.get(ip, (now, 0))

    # reset every 60 seconds
    if now - window_start >= 60:
        window_start, count = now, 0

    if count >= RATE_LIMIT_PER_MIN:
        retry_after = 60 - (now - window_start)
        return False, max(retry_after, 1)

    _rate[ip] = (window_start, count + 1)
    return True, 0


# ----------------------------
# CAPTCHA — Cloudflare Turnstile
# ----------------------------
TURNSTILE_SECRET = os.getenv("TURNSTILE_SECRET_KEY", "")

async def verify_turnstile(token: str, ip: str) -> bool:
    # Dev convenience: if not configured, allow.
    # For real public deployment, set TURNSTILE_SECRET_KEY in env.
    if not TURNSTILE_SECRET:
        return True

    url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
    data = {"secret": TURNSTILE_SECRET, "response": token, "remoteip": ip}

    try:
        async with httpx.AsyncClient(timeout=5.0) as c:
            r = await c.post(url, data=data)
            j = r.json()
            return bool(j.get("success"))
    except Exception:
        return False


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "You are a precise technical assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=1,
    )
    return response.choices[0].message.content


def build_prompt_with_context_and_pdf(original_prompt: str, context: dict, pdf_text: str) -> str:
    lines = [original_prompt.strip(), ""]

    lines.append("Context:")
    if context:
        for k, v in context.items():
            lines.append(f"{k}: {v}")
    else:
        lines.append("(no extracted context)")

    lines.append("")
    lines.append("PDF:")
    lines.append(pdf_text or "(no pdf text extracted)")

    return "\n".join(lines)


@app.post("/analyze")
async def analyze(
    request: Request,
    prompt: str = Form(...),
    pdf: UploadFile = File(...),
    captcha_token: str = Form(""),
):
    # Get IP (works behind proxies if x-forwarded-for is set)
    ip = request.headers.get("x-forwarded-for", "").split(",")[0].strip() or request.client.host

    # Rate limit
    ok, retry_after = check_rate_limit(ip)
    if not ok:
        return {"error": f"Rate limited. Try again in {retry_after}s."}

    # CAPTCHA verify
    if not captcha_token:
        return {"error": "Missing captcha token."}

    captcha_ok = await verify_turnstile(captcha_token, ip)
    if not captcha_ok:
        return {"error": "Captcha failed."}

    pdf_bytes = await pdf.read()

    tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    try:
        tmp.write(pdf_bytes)
        tmp.flush()
        tmp_path = tmp.name
    finally:
        tmp.close()

    try:
        agg = ContextAggregator(prompt, tmp_path)

        augmented_prompt = build_prompt_with_context_and_pdf(
            prompt,
            agg.context,
            agg.text,
        )

        llm_output = call_llm(augmented_prompt)

        # NOTE: For public use, avoid returning augmented_prompt/raw_context (leaks PDF content).
        return {
            "output": llm_output,
        }

    except Exception as e:
        # Always return JSON error so frontend doesn't JSON.parse explode
        return {"error": str(e)}

    finally:
        try:
            os.remove(tmp_path)
        except Exception:
            pass