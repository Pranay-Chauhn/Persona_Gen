def build_description_prompt(text_chunk: str, trait: str):
    return f"""
You are a user persona assistant. Based on the Reddit activity below, extract solid, concise insights for the category: **{trait}**.

Instructions per trait:
- For "4-words" : Return 4 words which describes and users personality, humor, nature, behaviour.
- For "Behavior and Habits": Return 2-3 bullet points, each ~10 words, summarizing clear behavior patterns or routines.
- For "Goals and Needs": Return 1-2 short bullets (~10 words each) capturing user motivations or desires.
- For "Frustrations": Return exactly 2 clear frustration points (10 words each), inferred from tone or complaints.

Always base your output on the user's language or context in posts/comments. Do not speculate.

Response Format:
Category: {trait}
Points:
- <point 1>
- <point 2>
- ...
Evidence: <Quote or sentence from Reddit that supports your summary>

If there is not enough data to support this trait, say:
"Not enough evidence."

---
Reddit Activity:
\"\"\"
{text_chunk}
\"\"\"
"""