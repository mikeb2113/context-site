# backend/context_inserter.py
import tempfile
from csir.context_aggregator import ContextAggregator

def run_context_insertion(prompt: str, pdf_bytes: bytes) -> dict:
    """
    Adapts uploaded PDF bytes -> temp file path
    Calls your existing ContextAggregator exactly as-is
    """

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp:
        tmp.write(pdf_bytes)
        tmp.flush()

        agg = ContextAggregator(prompt, tmp.name)
        return agg.context