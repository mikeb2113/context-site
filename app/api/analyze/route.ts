import { NextResponse } from "next/server";
export const runtime = "nodejs";

export async function POST(req: Request) {
  const form = await req.formData();
  const prompt = String(form.get("prompt") ?? "");
  const pdf = form.get("pdf");

  if (!prompt.trim()) return NextResponse.json({ error: "Missing prompt" }, { status: 400 });
  if (!(pdf instanceof File)) return NextResponse.json({ error: "Missing PDF" }, { status: 400 });

  const forward = new FormData();
  forward.append("prompt", prompt);
  forward.append("pdf", pdf, pdf.name);

  const pyRes = await fetch("https://context-site.onrender.com/analyze", {
    method: "POST",
    body: forward,
  });

  const data = await pyRes.json();
  return NextResponse.json(data, { status: pyRes.status });
}