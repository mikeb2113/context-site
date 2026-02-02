import Link from "next/link";

export default function ExamplePage() {
  return (
    <div className="space-y-12 max-w-3xl">
      {/* Header */}
      <section className="space-y-3">
        <h1 className="text-6xl font-semibold">
          How it Works
        </h1>
      </section>

<div className="mt-8 space-y-5 text-neutral-800 text-base leading-relaxed">
  <p>
The purpose of this project is to extract relevant sections of an input document. These are 
then appended to the user’s prompt.
  </p>

  <p>
First, text is extracted from the input document. Pulling from a limited, predefined list of 
words, each sentence is ascribed stop gaps according to the roles words play in standard 
English. The types of words that are accounted for are:
Determiners
Prepositions
Conjunctions
Modifiers
Auxiliary words
Compositional words
  </p>

  <p>
Using this, it isolates the first noun-phrase or prepositional phrase from each sentence.
Using this, it can predict the section of a sentence that will contain the subject, without 
the need to define the subject with any certainty. This allows it to determine what a sentence 
is about without the need for neural models to learn domain-specific language. This also adds 
flexibility, identifying instances where a word in the query modifies the subject of a sentence, 
but does not look so deep as to find instances where it is a minor point.
  </p>

  <p>
Once stop-gaps have been added, only sentences that may be relevant to the query are analyzed. The full sentence is appended to the query as context for the LLM
  </p>
</div>

<section className="mt-16 max-w-3xl">
  <div className="grid gap-8 sm:grid-cols-2">
    {/* Card 1 */}
<Link
  href="/example"
  className="block h-[260px] rounded-2xl border border-neutral-800 bg-[#1f1f1f] overflow-hidden hover:opacity-90 transition"
>
  <div className="h-full flex items-center justify-center">
    <span className="text-[#ce7807] text-5xl font-semibold tracking-tight">
      {"{Example:}"}
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