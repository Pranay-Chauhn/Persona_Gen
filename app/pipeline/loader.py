from urllib.parse import urlparse
import praw
import re
import os
from dotenv import load_dotenv

load_dotenv()

def init_reddit_client() :
    return praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("SECRET_KEY"),
        user_agent="reddit-persona-script by u/CryptographerOld7576",
        username=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD")
    )

def clean_text(text : str) -> str :
    text = re.sub(r"http\S+" , "", text) # remove URLs
    text = re.sub(r"\[.*?\]\(.*?\)", "", text) # remove markdown
    text = re.sub(r"[^\x00-\x7F]+", "", text) # remove emojis
    text = re.sub(r"\s{2,}","",text) # Extra space
    return text.strip()
def filter_clean(text_blocks, min_len=30) :
    return [clean_text(t['text']) for t in text_blocks if len(t['text']) > min_len]

def extract_username(reddit_user : str) -> str :
    """
    Extract Reddit username from a Reddit profile URl.
    Example : https://www.reddit.com/user/jeon_beom/
    """
    path = urlparse(reddit_user).path
    segments = path.strip('/').split('/')
    if "user" in segments :
        return segments[segments.index("user")+1]
    else :
        return print("Invalid Reddit user URL")

def loader(username : str ,limit=1000, output_dir = "D:\\Projects\\Persona_Gen\\app\\outputs",) :
    """
    Fetch recent comments and posts submissions from a Reddit User
    Then return: (comments-> list, posts->list)
    """
    reddit = init_reddit_client()
    redditor = reddit.redditor(username)

    # Fetch Comments 
    comments = []
    for comment in redditor.comments.new(limit=limit) :
        comments.append({
            "text" : comment.body,
            "permalink" : f"https://www.reddit.com{comment.permalink}"
        })
    
    # Fetch Submissions
    posts = []
    for post in redditor.submissions.new(limit=limit) :
        posts.append({
            "text" : (post.title or "") + "\n" + (post.selftext or ""),
            "permalink" : f"https://www.reddit.com{post.permalink}"
        })
    # Clean the Comments and Post
    user_data =  filter_clean(comments + posts)

    print('Creating File...')
    output_dir = output_dir
    filename = "user_data.txt"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir,filename)

    with open(file_path,"w", encoding="utf-8") as f :
        f.write("\n".join(user_data))

    return print(f"Saved file user_data.txt at {output_dir}")



