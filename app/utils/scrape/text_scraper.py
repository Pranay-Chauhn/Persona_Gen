import praw
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


def get_user_data(username : str ,limit=1000) :
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
            "text" : comment,
            "permalink" : f"https://www.reddit.com{comment.permalink}"
        })
    
    # Fetch Submissions
    posts = []
    for post in redditor.submissions.new(limit=limit) :
        posts.append({
            "text" : (post.title or "") + "\n" + (post.selftext or ""),
            "permalink" : f"https://www.reddit.com{post.permalink}"
        })
    return comments, posts




