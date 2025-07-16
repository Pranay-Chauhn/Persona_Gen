"""import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)"""

from app.utils.scrape.url_scraper import extract_username
from app.utils.scrape.text_scraper import get_user_data

url = "https://www.reddit.com/user/jeon_beom/"

username = extract_username(url)
print(f'Extracted UserName : {username}')

comments, posts = get_user_data(username)

print(f"Comments: {len(comments)}")
for i, c in enumerate(comments[:3]):
    print(f"\n[Comment {i+1}]\n{c['text']}\n→ {c['permalink']}")

print(f"\nPosts: {len(posts)}")
for i, p in enumerate(posts[:3]):
    print(f"\n[Post {i+1}]\n{p['posts']}\n→ {p['permalink']}")
