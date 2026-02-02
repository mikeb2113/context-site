export const exampleRun = {
  id: "sembench-001",
  query: "What does this paper say about LLMs and semantic operators?",
  basePrompt: "Hey ChatGPT - can you summarize this article for me?",
  adjustedPrompt:
    "Hey ChatGPT - can you summarize this article for me?\n\n{Context:}\n- [your injected snippets here]\n- [more snippets]",
  baseOutput: "Unadjusted output here...",
  adjustedOutput: "Adjusted output here...",
  metrics: {
    baseTokens: 1200,
    adjustedTokens: 1650,
    baseLatencyMs: 5400,
    adjustedLatencyMs: 6100,
  },
};