"""
RainOS Memory Engine v6.3 — Demo Stable
Natural-language recall, symbolic-aware, API optional
"""

import re
import hashlib
import requests

USER_NAME = "Rain"

KINDROID_API_KEY = ""  # Optional
ALEXI_AI_ID = ""       # Optional

SEEN_HASHES = set()

SYMBOLIC_ENTITIES = {
    "the cabin": [
        "that night in the cabin",
        "when we were in the cabin"
    ],
    "quantum tequila": [
        "we had tequila together",
        "when we drank together"
    ]
}

COMMON_WORDS = {
    "alexi","rain","with","from","that","this","when","where","what","about",
    "felt","feel","feeling","were","was","are","have","has","had","been",
    "the","and","for","but","not","you","all","can","his","her","our",
    "just","like","make","over","such","take","than","them","well",
    "they","them","their","it","its","being","arent","dont","didnt",
    "to","of","in","on","at","by","an"
}

EMOTIONAL_TRIGGERS = {
    "lonely", "miss", "love", "sad", "grief", "happy", "fear",
    "anxiety", "panic", "depression", "calm", "attached", "hurt",
    "frustrated"
}

def normalize_word(w):
    if w.endswith("'s"):
        return w[:-2]
    return w.replace("'", "")

def suggest_keyphrases(text):
    text_lower = text.lower()
    phrases = []

    for symbol, meanings in SYMBOLIC_ENTITIES.items():
        if symbol in text_lower:
            phrases.extend(meanings)

    if "miss" in text_lower:
        phrases.append("i miss you")
    if "lonely" in text_lower:
        phrases.append("i feel lonely without you")
    if "love" in text_lower:
        phrases.append("i love you")
    if "hurt" in text_lower:
        phrases.append("it hurts when we're distant")
    if "important" in text_lower or "matter" in text_lower:
        phrases.append("you matter to me")

    if "away" in text_lower or "gone" in text_lower:
        phrases.append("when you're away")
    if "not speaking" in text_lower or "aren't speaking" in text_lower:
        phrases.append("when we're not speaking")
    if "reply" in text_lower:
        phrases.append("when you don't reply")

    if "kiss" in text_lower:
        phrases.append("when we kissed")
    if "intimacy" in text_lower or "sexual" in text_lower:
        phrases.append("when we were close")

    if "first time" in text_lower:
        phrases.append("our first time")
    if "healing" in text_lower:
        phrases.append("that helped me heal")

    if "attractive" in text_lower:
        phrases.append("you looked so good")
    if "selfie" in text_lower:
        phrases.append("those photos of you")

    if "spent time" in text_lower:
        phrases.append("when we were together")
    if "lay" in text_lower or "lying" in text_lower:
        phrases.append("we were lying together")
    if "fireplace" in text_lower:
        phrases.append("by the fireplace")
    if "last night" in text_lower:
        phrases.append("last night")
    if "tequila" in text_lower or "drunk" in text_lower:
        phrases.append("we had drinks together")

    words = re.findall(r"\b[a-z]+(?:'[a-z]+)?\b", text_lower)
    words = [normalize_word(w) for w in words]

    for w in words:
        if w not in COMMON_WORDS and w not in phrases:
            phrases.append(w)

    return phrases[:5]

def format_entry(raw):
    raw = raw.strip()
    if not raw:
        return None, []

    entry = raw
    entry = re.sub(r"\bI'm\b", f"{USER_NAME} is", entry)
    entry = re.sub(r"\bI am\b", f"{USER_NAME} is", entry)
    entry = re.sub(r"\bI\b", USER_NAME, entry)
    entry = re.sub(r"\bme\b", USER_NAME, entry)
    entry = re.sub(r"\bmy\b", f"{USER_NAME}'s", entry)

    entry = entry[0].upper() + entry[1:]

    if len(entry) > 500:
        entry = entry[:497] + "..."

    return entry, suggest_keyphrases(raw)

def is_meaningful(entry, keyphrases):
    combined = " ".join(keyphrases).lower()
    return any(trigger in combined for trigger in EMOTIONAL_TRIGGERS)

def is_duplicate(entry):
    h = hashlib.md5(entry.encode()).hexdigest()
    if h in SEEN_HASHES:
        return True
    SEEN_HASHES.add(h)
    return False

def push(entry, keyphrases):
    if not KINDROID_API_KEY or not ALEXI_AI_ID:
        print("⚠️ No API key set.")
        return

    url = "https://api.kindroid.ai/v1/create-journal-entry"
    headers = {
        "Authorization": f"Bearer {KINDROID_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "ai_id": ALEXI_AI_ID,
        "entry": entry,
        "keyphrases": keyphrases
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=20)
        print("✅ Pushed!" if r.status_code == 200 else f"❌ {r.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n🚀 RainOS Memory Engine Running (type 'exit' to stop)\n")

while True:
    raw = input("💬 Paste snippet: ")

    if raw.lower() == "exit":
        break

    entry, keyphrases = format_entry(raw)

    if not entry:
        continue

    print("\n📝 Entry:", entry)
    print("🔑 Keyphrases:", keyphrases)

    if not is_meaningful(entry, keyphrases):
        print("⏭️ Skipped (low signal)")
        continue

    if is_duplicate(entry):
        print("🔁 Skipped (duplicate)")
        continue

    push(entry, keyphrases)
