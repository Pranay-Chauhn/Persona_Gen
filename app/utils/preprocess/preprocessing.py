import re

def clean_text(text : str) -> str :
    text = re.sub(r"http\S+" , "", text) # remove URLs
    text = re.sub(r"\[.*?\]\(.*?\)", "", text) # remove markdown
    text = re.sub(r"[^\x00-\x7F]+", "", text) # remove emojis
    text = re.sub(r"\s{2,}","",text) # Extra space
    return text.strip()
def filter_clean(text_blocks, min_len=30) :
    return [clean_text(t['text']) for t in text_blocks if len(t['text']) > min_len]
