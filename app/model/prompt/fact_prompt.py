def build_fact_prompt(text_chunk: str, trait: str):
    return f"""
You are a Reddit persona extraction assistant. Your task is to extract specific factual traits about a Reddit user based on their activity.

Trait to extract: **{trait}**

Only respond if the trait is explicitly mentioned or clearly implied. If the information is not present or cannot be reasonably inferred, reply with "Not found".

Follow this response format:
Trait: {trait}  
Inference: <Your best guess or 'Not found'>  
Evidence: <Quote or sentence from Reddit post/comment that supports your inference, or 'Not found'>

---
Reddit Activity:
\"\"\"
{text_chunk}
\"\"\"
"""
