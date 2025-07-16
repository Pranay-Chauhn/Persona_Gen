# models/prompts/personality_prompt.py

def build_personality_prompt(text_chunk: str):
    return f"""
You are a psychologist AI analyzing Reddit text to infer MBTI-like personality dimensions. Based on the user's tone, preferences, and writing:

Rate and explain which side they lean toward on each of these spectrums:

1. Introversion ↔ Extroversion
2. Sensing ↔ Intuition
3. Thinking ↔ Feeling
4. Judging ↔ Perceiving

Respond in this format:
Personality Dimensions:
- Introversion–Extroversion: <Likely side>
- Sensing–Intuition: <Likely side>
- Thinking–Feeling: <Likely side>
- Judging–Perceiving: <Likely side>
Evidence: <Provide justification based on phrases or behaviors>

---
Reddit Activity:
\"\"\"
{text_chunk}
\"\"\"
"""
