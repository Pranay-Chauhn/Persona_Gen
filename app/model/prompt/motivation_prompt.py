# models/prompts/motivation_prompt.py

def build_motivation_prompt(text_chunk: str):
    return f"""
You are an AI assistant analyzing Reddit user motivations based on their writing.

Rate the following motivational aspects from 1 to 10, based on how much the user seems to value them:

- Convenience
- Speed
- Comfort
- Wellness
- Preference (control over choices)
- Dietary Needs

Respond in this format:
Trait Ratings:
- Convenience: #
- Speed: #
- Comfort: #
- Wellness: #
- Preference: #
- Dietary Needs: #
Evidence: <Cite exact sentences or phrases used for these scores>

---
Reddit Activity:
\"\"\"
{text_chunk}
\"\"\"
"""
