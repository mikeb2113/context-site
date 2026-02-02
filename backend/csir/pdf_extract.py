from pathlib import Path
import PyPDF2
import html
import pdfplumber
import re
import unicodedata
from . import libs
from pathlib import Path

LIB_WORDS = libs.DET | libs.PREP | libs.CONJ | libs.COMP | libs.MOD | libs.AUX

def pdf_to_text(path: str) -> str:
    """Extract raw text from a PDF as one big string."""
    path = Path(path)
    text_chunks = []

    with path.open("rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            # Keep page markers so you can later track where shapes came from
            #text_chunks.append(f"\n\n=== PAGE {page_num + 1} ===\n\n{page_text}")
            decode = clean_text(page_text)
            text_chunks.append(decode)

    return "\n".join(text_chunks)

def unstick_library_prefixes(
    text: str,
    min_lib_len: int = 1,   # skip tiny libs like "a", "in", "to"
) -> str:
    """
    Try to fix glued cases like 'theking' -> 'the king',
    using per-prefix whitelists of valid words.

    Logic:
      - At the start of a letter-run, check if it begins with any library word
        of length >= min_lib_len that has a whitelist.
      - Extract the full word (letters only).
      - If full word == lib word: leave as-is.
      - Else if full word is in that prefix's whitelist: leave as-is.
      - Else: split into 'lib' + ' ' + 'tail'.
    """

    # Only consider library words we actually have whitelists for,
    # and that meet the length requirement
    safe_libs = [
        w for w in LIB_WORDS
        if len(w) >= min_lib_len and w in libs.PREFIX_WHITELIST
    ]

    # Try longer library words first
    lib_sorted = sorted(safe_libs, key=len, reverse=True)

    out = []
    i = 0
    n = len(text)

    def is_alpha(ch: str) -> bool:
        return ch.isalpha()

    while i < n:
        ch = text[i]

        if not is_alpha(ch):
            out.append(ch)
            i += 1
            continue

        prev = text[i-1] if i > 0 else " "

        # Only consider at the *start* of a word-like run
        if not is_alpha(prev):
            lowered_slice = text[i:].lower()
            matched = False

            for w in lib_sorted:
                wl = len(w)
                if wl <= len(lowered_slice) and lowered_slice.startswith(w):
                    # Found a library prefix at word start
                    j = i + wl

                    # Consume the full word: lib + tail letters
                    k = j
                    while k < n and is_alpha(text[k]):
                        k += 1

                    full_word = text[i:k]
                    full_lower = full_word.lower()

                    whitelist = libs.PREFIX_WHITELIST.get(w, set())

                    if full_lower == w:
                        # Just the lib word itself, e.g. "the "
                        out.append(full_word)
                        i = k
                        matched = True
                        break

                    if full_lower in whitelist:
                        # Legit word like "theorem", "overall", etc. -> don't split
                        out.append(full_word)
                        i = k
                        matched = True
                        break

                    # Otherwise treat as glued and split: "<lib><tail>" -> "<lib> <tail>"
                    lib_part = text[i:i+wl]
                    tail_part = text[i+wl:k]
                    out.append(lib_part)
                    out.append(" ")
                    out.append(tail_part)
                    i = k
                    matched = True
                    break

            if matched:
                continue

        # Default: just copy the character
        out.append(ch)
        i += 1

    return "".join(out)

# def extract_pdf_text(path: str) -> str:
#     path = Path(path)
#     text_chunks = []

#     with pdfplumber.open(path) as pdf:
#         for page in pdf.pages:
#             # layout=True tries to respect glyph positions
#             page_text = page.extract_text(layout=True) or ""
#             text_chunks.append(page_text)

#     raw = "\n".join(text_chunks)
#     return clean_text(raw)

def clean_text(text: str) -> str:
    # Decode HTML entities like &quot;
    text = html.unescape(text)

    # Normalize unicode (fancy quotes, compatibility forms)
    text = unicodedata.normalize("NFKC", text)

    # Normalize weird whitespace: turn all whitespace into single spaces
    text = re.sub(r"\s+", " ", text)
    text = text.replace(",", "").replace("?", "")
    # Remove commas
    text = text.replace(",", "")

    return text.strip()
"""
&quot;Along the shore the cloud waves break,
The twin suas sink behind the lake.
The shadows lengthen
In Carcosa.
"""