# models/prompts/description_prompt.py

def build_description_prompt(text_chunk: str, category: str):
    return f"""
Analyze the Reddit activity below and extract {category.lower()} about the user.

Respond in the format:
Category: {category}
Points:
- <Point 1>
- <Point 2>
- ...
Evidence: <Cite key sentences or phrases used to derive this info>

If insufficient data is found, say: "Not enough evidence."

---
Reddit Activity:
\"\"\"
{text_chunk}
\"\"\"
"""
