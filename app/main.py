from app.pipeline.loader import extract_username, loader
from app.pipeline.chunker import chunker
username = extract_username("https://www.reddit.com/user/kojied/")
loader(username)
chunker("D:/Projects/Persona_Gen/app/outputs/user_data.txt",chunk_size = 5000, chunk_overlap=300)