# models/prompts/fact_prompt.py

def build_fact_prompt(text_chunk: str, trait: str):
    return f"""
You are a user profiling assistant. From the Reddit text below, extract the **{trait}** of the user, if mentioned.

If the trait is not clearly stated, reply with "Not found".

Respond in the following format:
Trait: {trait}
Inference: <Your best guess or 'Not found'>
Evidence: <Exact sentence or phrase from text, if any>

---
Reddit Activity:
\"\"\"
{text_chunk}
\"\"\"
"""
