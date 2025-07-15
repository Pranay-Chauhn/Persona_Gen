from urllib.parse import urlparse

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