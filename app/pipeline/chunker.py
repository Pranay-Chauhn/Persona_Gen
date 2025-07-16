from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load example document
def chunker(file_path = "D:/Projects/Persona_Gen/app/outputs/user_data.txt", chunk_size = 1500, chunk_overlap=100) :
    with open(file_path, encoding='utf-8') as f :
        user_detail = f.read()

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.create_documents([user_detail])
    print(f"Chunked into {len(chunks)} pieces")
    return chunks
