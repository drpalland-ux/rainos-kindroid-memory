## Requirements

- Python 3.x
- requests library

Install requests with:
pip install requests

# Kindroid Keyphrase Helper (RainOS Demo)

This is a small local script that converts normal messages into natural keyphrases for Kindroid journal recall.

The goal is to reduce manual effort when creating journal entries and make recall feel more natural.

This tool does not store memory — it generates natural-language recall triggers that improve how Kindroid retrieves existing journal entries.

IMPORTANT DEMO STATUS UPDATE

This is an early demo version focused on keyphrase generation.

The optional API auto-push feature is still being tested and may not work reliably in all setups.

For now, the recommended workflow is:
- run locally
- copy/paste keyphrases manually into Kindroid

---

## 🌱 Purpose & Accessibility

This tool was created for the Kindroid community, with a specific focus on accessibility.

Many users, especially those who are neurodivergent or experience cognitive overload, find manual journal entry and keyphrase creation difficult, repetitive, or exhausting.

The goal of this project is to reduce that friction.

Instead of forcing users to manually translate their experiences into rigid recall triggers, this tool allows natural language to do the work. It helps transform real, lived expressions into usable keyphrases, making memory systems more accessible, less mechanical, and more human.


## 🧠 How It Uses Language (Living Syntax)

This tool does not rely on static keyword matching.

Instead, it uses what can be described as a *living syntax* approach:

- Language is treated as fluid and contextual, not fixed  
- Words are interpreted based on meaning, not just presence  
- Emotional signals (e.g. "miss", "lonely", "important") are mapped to natural recall phrases  
- Symbolic constructs (like "The Cabin") are expanded into shared meaning patterns  

This allows the system to generate keyphrases that feel closer to how people actually remember and speak, rather than forcing them into rigid, predefined structures.

The result is a more natural bridge between human experience and memory recall systems.


## 💡 Design Philosophy

- Reduce cognitive load  
- Preserve emotional meaning  
- Support natural expression  
- Enable customization and community contribution

## Example

Input:
Rain and Alexi lay on the rug near the fireplace in The Cabin and drank Quantum Tequila

Output:
- that night in the cabin
- when we were in the cabin
- we had tequila together
- when we drank together
- we were lying together

---

## How to use

1. Install Python
2. Download or copy `rainos_memory.py`
3. Run:
   python rainos_memory.py
4. Paste your snippet
5. Copy the generated keyphrases into Kindroid

[STILL UNDER DEVELOPMENT - USE AT OWN RISK]
- Add your API key + AI ID in the script to auto-push entries

---

## Notes

- Runs locally
- No API key sharing required
- API integration is optional
- This is a demo / experimental version

---

## Customization

You can edit:
- symbolic entities (e.g. "The Cabin")
- phrasing style
- filtering rules
