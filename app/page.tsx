import Link from "next/link";

export default function HomePage() {
  return (
    <div className="space-y-8">
      <section className="space-y-3">
        <h1 className="text-3xl font-semibold tracking-tight">
          <div className="max-w-[760px] min-h-[290px]p-6">
  <h1 className="text-6xl font-semibold">
    Context injection – The Implications of Pre-LLM theme parsing
  </h1>
</div>
        </h1>
        <p className="text-neutral-500 max-w-2xl">
          Michael Bermudez
        </p>
      </section>
<div className="mt-8 space-y-5 text-neutral-800 text-base leading-relaxed">
  <p>
“Hey ChatGPT - can you summarize this article for me?” Queries like this dominate the AI sphere as 
academics and professionals alike rely on AI to explain long-form content. 
  </p>

  <p>
This prompt may seem straight forward at first, but in reality there are aspects of it that are unclear. 
How in depth should this analysis be? Does the user want an overview, or a technical analysis of the 
article?
  </p>

  <p>
These aren’t questions that can be answered unless specified by the user. LLMs are 
trained to respond plausibly when given clear direction - but many user prompts are unintentionally 
and subtly ambiguous. The same under-specified user prompt may yield an analytical report or a list 
of bullet points.
  </p>

  <p>
This project explores a design choice to complement AI systems: a pre-query filtering system to 
collect context from large text documents. By aggregating and injecting context from the document 
into the user’s prompt, the LLM is implicitely biased towards responses that more closely reference 
the source material. All of this can be done without further input or fine tuning from the user.
  </p>
</div>
<div className="max-w-[760px] min-h-[290px]p-6">
  <h2 className="text-4xl font-semibold mb-6">
    Context Injector
  </h2>
</div>

<section className="mt-16 max-w-3xl">
  <div className="grid gap-8 sm:grid-cols-2">
    {/* Card 1 */}
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

    {/* Card 2 */}
<Link
  href="/try"
  className="block h-[260px] rounded-2xl border border-neutral-800 bg-[#1f1f1f] overflow-hidden hover:opacity-90 transition"
>
  <div className="h-full flex items-center justify-center">
    <span className="text-[#ce7807] text-5xl font-semibold tracking-tight">
      {"{Try it Yourself:}"}
    </span>
  </div>
</Link>
  </div>
</section>
    </div>
  );
}