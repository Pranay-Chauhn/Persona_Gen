from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda
from typing import List

from app.model.prompt.description_prompt import build_description_prompt

def run_summary_chain(llm, documents: List[Document], category: str):
    """
    Runs a modern LangChain Runnable-based map-reduce summarization chain
    to extract descriptive traits like '4 Words', 'Goals', 'Habits', etc.
    """

    # 🔹 Step 1: MAP Prompt
    map_prompt = PromptTemplate.from_template(
        build_description_prompt("{text_chunk}", category)
    )
    map_chain = map_prompt | llm | RunnableLambda(lambda x: x.content)

    # 🔹 Step 2: Run MAP step on all chunks
    mapped_outputs = []
    for doc in documents:
        response = map_chain.invoke({"text_chunk": doc.page_content})
        mapped_outputs.append(response)

    # 🔹 Step 3: REDUCE Prompt (combine map results)
    combined_text = "\n\n".join(mapped_outputs)
    reduce_prompt = PromptTemplate.from_template(f"""
You are a helpful analyst building a user persona.

Below are extracted {category} trait clues from different Reddit posts/comments. Summarize the top 4–6 points in bullet format with concise reasoning.

Clues:
{{combined_chunks}}
""")
    reduce_chain = reduce_prompt | llm | RunnableLambda(lambda x: x.content)

    result = reduce_chain.invoke({"combined_chunks": combined_text})
    return result
