import os
"""import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)"""

from app.utils.scrape.url_scraper import extract_username
from app.utils.scrape.text_scraper import get_user_data
from app.utils.preprocess.preprocessing import filter_clean

url = "https://www.reddit.com/user/jeon_beom/"

username = extract_username(url)
print(f'Extracted UserName : {username}')

comments, posts = get_user_data(username)

"""print(f"Comments: {len(comments)}")
for i, c in enumerate(comments[:3]):
    print(f"\n[Comment {i+1}]\n{c['text']}\n→ {c['permalink']}")

print(f"\nPosts: {len(posts)}")
for i, p in enumerate(posts[:3]):
    print(f"\n[Post {i+1}]\n{p['text']}\n→ {p['permalink']}")
"""
# Clean the Comments and Post
user_data =  filter_clean(comments + posts)

print('Creating File...')
output_dir = "D:\\Projects\\Persona_Gen\\app\\outputs"
filename = "user_data.txt"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir,filename)

with open(file_path,"w", encoding="utf-8") as f :
    f.write("\n".join(user_data))

"""print('Creating File...')
output_dir = "D:\\Projects\\Persona_Gen\\app\\outputs"
filename = "userposts.txt"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir,filename)

with open(file_path,"w", encoding="utf-8") as f :
    f.write("\n".join(str(comment['text']) for comment in comments))
print("Creating UserPosts....")
with open(file_path,"a", encoding="utf-8") as f :
    f.write("\n".join(str(post['text']) for post in posts))
"""