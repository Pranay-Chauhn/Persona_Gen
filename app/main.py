from dotenv import load_dotenv
from app.pipeline.loader import extract_username, loader
from app.pipeline.chunker import chunker
from app.pipeline.writer import save_persona
from app.pipeline.controller import run_persona_extraction
from langchain_community.chat_models import ChatOpenAI
import os

# load env
load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("LLM_API_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model_name=os.getenv("LLM_MODEL_NAME"),
    timeout=360
)

# Get Data
username = extract_username("https://www.reddit.com/user/kojied/")
loader(username)
chunks = chunker("D:/Projects/Persona_Gen/app/outputs/user_data.txt",chunk_size = 5000, chunk_overlap=300)

# Run Pipeline
persona = run_persona_extraction(llm, chunks)

# Save Output 
save_persona(persona)