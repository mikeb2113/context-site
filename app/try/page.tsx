"use client";

import Link from "next/link";
import { useRef, useState } from "react";
import { Turnstile } from "@marsidev/react-turnstile";

export default function ExamplePage() {
  const [output, setOutput] = useState("Output will appear here…");
  const [prompt, setPrompt] = useState("");
  const [fileName, setFileName] = useState("");
  const [pdfFile, setPdfFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [captchaToken, setCaptchaToken] = useState("");

  const fileInputRef = useRef<HTMLInputElement>(null);

  async function onRun() {
    if (!prompt.trim()) {
      setOutput("Please enter a prompt.");
      return;
    }
    if (!pdfFile) {
      setOutput("Please choose a PDF.");
      return;
    }
    if (!captchaToken) {
      setOutput("Please complete the human check (captcha).");
      return;
    }

    setLoading(true);
    setOutput("Running…");

    try {
      const form = new FormData();
      form.append("prompt", prompt);
      form.append("pdf", pdfFile);
      form.append("captcha_token", captchaToken); // ✅ send token to /api/analyze

      const res = await fetch("/api/analyze", {
        method: "POST",
        body: form,
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data?.error || "Request failed");

      const out =
        typeof data.output === "string"
          ? data.output
          : JSON.stringify(data.output, null, 2);

      setOutput(out ?? "(no output returned)");
    } catch (err: any) {
      setOutput(`Error: ${err.message ?? String(err)}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-12 max-w-3xl">
      <section className="space-y-3">
        <h1 className="text-6xl font-semibold">Try it Yourself</h1>
      </section>

      <div className="mt-8 space-y-5 text-neutral-800 text-base leading-relaxed">
        <section className="space-y-2">
          <label className="text-sm text-neutral-700">Enter your prompt here:</label>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Can you explain…"
            className="
              w-full h-[110px] rounded-xl bg-neutral-100 px-5 py-4
              text-neutral-900 placeholder:text-neutral-500 outline-none
              ring-1 ring-neutral-200 focus:ring-2 focus:ring-neutral-400 resize-none
            "
          />
        </section>

        <section className="space-y-2">
          <label className="text-sm text-neutral-700">Insert a PDF file:</label>

          <div className="flex gap-3">
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              className="rounded-xl bg-neutral-900 px-5 py-3 text-sm text-white hover:bg-neutral-800 transition"
            >
              Choose a file
            </button>

            <div className="flex-1 rounded-xl bg-neutral-100 px-5 py-3 text-sm text-neutral-700 ring-1 ring-neutral-200">
              {fileName || "No file selected"}
            </div>
          </div>

          <input
            ref={fileInputRef}
            type="file"
            accept="application/pdf"
            className="hidden"
            onChange={(e) => {
              const file = e.target.files?.[0] ?? null;
              setPdfFile(file);
              setFileName(file ? file.name : "");
            }}
          />
        </section>

        {/* ✅ Turnstile widget MUST be inside the rendered JSX */}
        <section className="space-y-2">
          <label className="text-sm text-neutral-700">Human check:</label>

          <Turnstile
            siteKey={process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY!}
            onSuccess={(token) => setCaptchaToken(token)}
            onExpire={() => setCaptchaToken("")}
            onError={() => setCaptchaToken("")}
          />
        </section>

        <div className="flex gap-3">
          <button
            type="button"
            disabled={loading}
            onClick={onRun}
            className="rounded-xl bg-[#ce7807] px-5 py-3 text-sm text-black hover:opacity-90 transition disabled:opacity-60"
          >
            {loading ? "Running…" : "Run"}
          </button>

          <button
            type="button"
            onClick={() => setOutput("")}
            className="rounded-xl bg-neutral-200 px-5 py-3 text-sm text-neutral-900 hover:bg-neutral-300 transition"
          >
            Clear
          </button>
        </div>

        <section className="space-y-2">
          <label className="text-sm text-neutral-700">Output:</label>
          <div className="w-full h-[220px] rounded-xl bg-neutral-100 px-5 py-4 text-neutral-900 ring-1 ring-neutral-200 overflow-y-auto whitespace-pre-wrap text-sm">
            {output}
          </div>
        </section>
      </div>

      {/* your links unchanged */}
      <section className="mt-16 max-w-3xl">
        <div className="grid gap-8 sm:grid-cols-2">
          <Link
            href="/technical"
            className="block h-[260px] rounded-2xl border border-neutral-800 bg-[#1f1f1f] overflow-hidden hover:opacity-90 transition"
          >
            <div className="h-full flex items-center justify-center">
              <span className="text-[#ce7807] text-5xl font-semibold tracking-tight">
                {"{How it Works:}"}
              </span>
            </div>
          </Link>

          <Link
            href="/"
            className="block h-[260px] rounded-2xl border border-neutral-800 bg-[#1f1f1f] overflow-hidden hover:opacity-90 transition"
          >
            <div className="h-full flex items-center justify-center">
              <span className="text-[#ce7807] text-5xl font-semibold tracking-tight">
                {"{Home:}"}
              </span>
            </div>
          </Link>
        </div>
      </section>
    </div>
  );
}