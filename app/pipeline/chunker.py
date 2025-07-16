from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load example document

with open(r"D:\Projects\Persona_Gen\app\outputs\user_data.txt", "r", encoding='utf-8') as f:
    user_detail = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.create_documents([user_detail])

