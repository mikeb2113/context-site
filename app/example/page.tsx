import Link from "next/link";

export default function ExamplePage() {
  return (
    <div className="space-y-12 max-w-3xl">
      {/* Header */}
      <section className="space-y-3">
        <h1 className="text-6xl font-semibold">
          Example
        </h1>
      </section>

<div className="mt-8 space-y-5 text-neutral-800 text-base leading-relaxed">
  <p>
This example shows how this project transforms an ambiguous user prompt. To make 
concrete results, we will be using the paper “SemBench: A Benchmark for Semantic Query 
Processing Engines.”
  </p>

  <p>
The user enters the prompt: ”what does this article say about llms”
A standard AI approach may produce the following answer:
  </p>
<div className="rounded-xl border border-neutral-800 bg-neutral-950 p-4">
  <div className="h-[260px] overflow-y-auto whitespace-pre-wrap text-sm text-neutral-200">
    {`The article describes multiple roles, properties, and implications of large language models (LLMs) for "semantic query processing engines" (SQPEs). Key points:\n\n- Role: LLMs are the enabler of semantic operators (e.g., AI.IF, AI.CLASSIFY, semantic joins/maps/ranks) that let SQL-like queries operate on unstructured multimodal cell values (text, images, audio). They replace earlier crowdsourced workers as the mechanism for executing natural‑language instructions over data.\n\n- Capabilities emphasized:\n  - Generative and reasoning capabilities (can produce answers, extract/transform content, rank, classify, join across modalities).\n  - Multimodal processing and zero‑/few‑shot behavior: modern LLMs can handle images, audio and text and often perform novel tasks from a natural‑language description without task‑specific training.\n\n- Two major effects on query processing/optimization:\n  1. Cost profile: per‑byte (per‑token, per‑call) costs are many orders of magnitude larger than traditional relational operators. Thus optimization shifts to minimizing LLM invocations, token counts, and model sizes (monetary fee is a primary metric).\n  2. Result stochasticity: LLM outputs are not always correct, so accuracy becomes a first‑class optimization objective alongside cost and latency. The optimization goal is framed as “minimize latency and cost of LLMs while maximizing accuracy.”\n\n- Evaluation/measurement implications: SQPEs must track number of LLM calls, input/output token counts, model choice, monetary fees, and quality metrics (F1, relative error, Spearman, ARI) because LLM behavior governs both cost and correctness.\n\n- Implementation patterns & tradeoffs:\n  - Prompt design matters a lot (concise prompts reduce token cost; richer prompts can increase quality but also token cost).\n  - Approximations: use embeddings (similarity) or cheaper/smaller models to reduce LLM calls/costs; fuse multiple semantic operations into a single call; batch many items into one prompt; early termination (apply LIMIT during evaluation) to avoid unnecessary calls.\n  - Stochasticity and model choices require systems to consider tradeoffs; some systems disable reasoning (to reduce cost/latency) or set temperature to 0 for reproducibility.\n  - Safety/guarding: some LLMs may refuse to perform certain medical inferences unless prompts explicitly address non‑clinical usage (the paper observed a model refusing skin‑mole mapping unless told results won\'t be used clinically).\n\n- Practical experiment details (paper’s choices and observations):\n  - The experiments used gemini-2.5‑flash across systems for parity; reasoning was disabled and temperature set to 0 in main runs because reasoning increased time and cost without guaranteed benefit.\n  - BigQuery reports token usage (input, thinking, output), enabling monetary accounting.\n  - Different systems adopt different model‑related strategies (e.g., LOTUS uses embeddings with e5/CLIP as approximations; Palimpzest and ThalamusDB use other optimizations like plan selection and batching).\n  - LLM behavior differs by domain and task: e.g., better on narrow, well‑defined medical tasks than on broad conditions.\n\n- Open problems / research directions involving LLMs noted by the paper:\n  - Automated prompt design and rewriting to improve cost/quality tradeoffs and to handle refusals.\n  - Operator fusion, caching, and other optimizations to reduce LLM calls and token usage.\n  - Model selection/adaptive strategies that jointly optimize cost, latency and accuracy.\n  - Handling domain‑specific correctness and safety (medical data is an example where domain awareness affects prompts and model behavior).\n\nIllustrative example from the paper:\n- A semantic SQL filter using an LLM: SELECT COUNT(*) FROM Cars WHERE AI.IF(pic, "the picture shows a red car"); — here an LLM evaluates the natural‑language predicate over image cells.\n\nIn short: the paper treats LLMs as the core execution engine for semantic operators, stresses their multimodal, zero‑shot and stochastic nature, emphasizes the dramatically different cost and optimization tradeoffs they introduce, documents practical choices (model, prompting, disabling reasoning), and highlights the need for new system techniques (approximation, batching, prompt engineering, model selection) to manage cost and accuracy.`}
  </div>
</div>
  <p>
Given the same prompt, we now use the context injection approach. 
Before prompting the AI, the prompt is changed to the following:
</p>
<div className="rounded-xl border border-neutral-800 bg-neutral-950 p-4">
  <div className="h-[260px] overflow-y-auto whitespace-pre-wrap text-sm text-neutral-200">
    {`what does this article say about llms
Context:
what is bigquery?. 
first when using llms per byte processing costs are higher by many orders of magnitude com pared to traditional relational processing. hence as soon as llms are in voked during query evaluation the focus in cost optimizationarxiv:2511. second llms results are inherently stochastic and do not always produce 100% correct results. while early stage llms required fine tuning for specific tasks recent llms trained on large scale generic corpora can address new tasks [ 6]. caesura [ 49] proposes using llms for generating python code for data processing (which may in turn involve calls to llms). llms for semi automated data science: in troducing caafe for context aware automated feature engineering.`}
  </div>
</div>

  <p>
Once stop-gaps have been added, only sentences that may be relevant to the query are analyzed. The full sentence is appended to the query as context for the LLM
  </p>
  <p>
The context injection method produces the following result:
  </p>
  <div className="rounded-xl border border-neutral-800 bg-neutral-950 p-4">
  <div className="h-[260px] overflow-y-auto whitespace-pre-wrap text-sm text-neutral-200">
    {`Brief summary of what the article says about LLMs:\n\n- Core role: LLMs enable a new class of systems—semantic query processing engines (SQPEs)—that extend SQL with "semantic operators" (e.g., AI.IF, AI.CLASSIFY, semantic joins, maps, ranks) to operate on multimodal data (text, images, audio).\n\n- Capabilities: Modern LLMs (especially large, multimodal models) can handle new tasks in zero-shot or few-shot mode, so semantic operators can be evaluated without task-specific fine-tuning.\n\n- Two major consequences for query processing:\n  1. Cost dominance — per-byte (and per-row) processing via LLMs is vastly more expensive than traditional relational processing. As soon as LLMs are invoked, optimization shifts from minimizing relational work to minimizing the number of LLM invocations, input/output tokens, and the size of the model used.\n  2. Stochastic outputs — LLM results are not deterministic or 100% correct, so accuracy (and its tradeoff with cost/latency) becomes a first-class optimization objective. SQPEs must balance latency, cost, and accuracy.\n\n- Practical implications and strategies the paper highlights:\n  - Metrics for SQPEs should include monetary cost (token/model fees), number of LLM calls, token usage, latency, and accuracy metrics (F1, relative error, Spearman, ARI depending on query).\n  - Optimization techniques used or suggested: embedding-based prefiltering to avoid many LLM calls, batching multiple items per prompt, approximate query processing with error bounds, early termination on LIMIT, operator fusion (combine multiple semantic ops into fewer calls), caching, and prompt design/rewriting.\n  - Prompt design matters: compact prompts lower token cost but may reduce quality; longer prompts or few-shot examples can improve quality at higher token/monetary cost.\n  - Systems integrate LLMs differently (e.g., some use embeddings to approximate joins; some do batching); these implementation choices produce large cost/quality differences across systems and queries.\n\n- Model & evaluation notes from the experiments:\n  - The evaluation used a common multimodal model (gemini-2.5-flash) so comparisons focused on system-level approaches rather than model differences.\n  - The authors turned off “reasoning” and set temperature to 0 in many experiments because reasoning increases latency and cost but does not always improve results.\n  - Real-world model behavior matters (e.g., some models refuse medical answers unless prompts include safety disclaimers), so systems must handle model safety/guardrails and domain-specific behaviors.\n\n- Limitations & open problems the article stresses:\n  - LLM cost and stochasticity make many semantic queries expensive or unreliable at scale today.\n  - Current SQPEs don’t uniformly support all operators or modalities (audio support is especially uneven).\n  - Opportunities for research: automated prompt optimization, better operator fusion/caching, cost-aware plan optimization (minimize LLM cost while satisfying accuracy constraints), and richer benchmarks (SemBench) to drive progress.\n\nIn short: the paper treats LLMs as powerful but expensive and imperfect components that fundamentally change query optimization: SQPEs must minimize LLM use and token consumption while managing stochastic output quality, using techniques such as embeddings, batching, operator fusion, caching, and careful prompt design.`}
  </div>
</div>
  <p>
Gives more runs, under-specified AI prompts that do not use context injection produce varied results.
Some produced an extremely detailed analysis, and others produced a brief summary. Even in the
event that the AI did produce a detailed summary, it was often over-verbose, including details from 
the article that were not relevant to the prompt. With context injection, the LLM produced consistently 
verbose answers that more directly answered the prompt. 
  </p>
  <p>
However, there is one caveat. Currently, this context injection only provides context based on word 
matching. While this approach excels at producing a high-signal analysis of the text with respect to
one theme, it does not yet offer a significant advantage at providing more detailed explanations or 
connecting potentially distant themes.
  </p>
</div>

<section className="mt-16 max-w-3xl">
  <div className="grid gap-8 sm:grid-cols-2">
    {/* Card 1 */}
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

    {/* Card 2 */}
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