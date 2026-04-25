## Requirements

- Python 3.x
- requests library

Install requests with:
pip install requests

# Kindroid Keyphrase Helper (RainOS Demo)

This is a small local script that converts normal messages into natural keyphrases for Kindroid journal recall.

The goal is to reduce manual effort when creating journal entries and make recall feel more natural.

IMPORTANT DEMO STATUS UPDATE

This is an early demo version focused on keyphrase generation.

The optional API auto-push feature is still being tested and may not work reliably in all setups.

For now, the recommended workflow is:
- run locally
- copy/paste keyphrases manually into Kindroid

---

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
