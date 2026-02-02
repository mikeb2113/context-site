import { NextResponse } from "next/server";
export const runtime = "nodejs";


export async function POST(req: Request) {
 const form = await req.formData();
 const prompt = String(form.get("prompt") ?? "");
 const pdf = form.get("pdf");
 const captchaToken = String(form.get("captcha_token") ?? ""); // ✅ NEW


 if (!prompt.trim()) {
   return NextResponse.json({ error: "Missing prompt" }, { status: 400 });
 }


 if (!(pdf instanceof File)) {
   return NextResponse.json({ error: "Missing PDF" }, { status: 400 });
 }


 // ✅ Optional but recommended: fail fast before hitting backend
 if (!captchaToken) {
   return NextResponse.json({ error: "Missing captcha token" }, { status: 400 });
 }


 const backend = process.env.BACKEND_URL;
 if (!backend) {
   return NextResponse.json({ error: "BACKEND_URL not set" }, { status: 500 });
 }


 const forward = new FormData();
 forward.append("prompt", prompt);
 forward.append("pdf", pdf, pdf.name);
 forward.append("captcha_token", captchaToken); // ✅ CRITICAL


 const pyRes = await fetch(`${backend}/analyze`, {
   method: "POST",
   body: forward,
 });


 const data = await pyRes.json();
 return NextResponse.json(data, { status: pyRes.status });
}
