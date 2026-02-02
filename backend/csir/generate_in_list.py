import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.merriam-webster.com/wordfinder/classic/begins/all/-1/in/"

def fetch_in_page(page_number: int) -> list[str]:
    url = f"{BASE_URL}{page_number}"
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    words = []
    # This selector depends on their HTML – you’ll need to inspect the page.
    # Example pattern – adjust as needed after you View Source:
    for li in soup.select("ul.word-list li a"):
        w = li.get_text(strip=True)
        if w and w.lower().startswith("in"):
            words.append(w.lower())
    return words

def build_in_whitelist_from_mw(max_pages: int = 10) -> set[str]:
    all_words = set()
    for page in range(1, max_pages + 1):
        words = fetch_in_page(page)
        if not words:
            break
        all_words.update(words)
        time.sleep(1)  # be polite, don't hammer
    return all_words

if __name__ == "__main__":
    in_words = build_in_whitelist_from_mw(max_pages=20)
    with open("in_whitelist.json", "w", encoding="utf-8") as f:
        json.dump(sorted(list(in_words)), f, ensure_ascii=False, indent=2)
    print(f"Collected {len(in_words)} 'in*' words.")