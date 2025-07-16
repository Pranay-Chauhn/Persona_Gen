from langchain.chains.combine_documents.refine import RefineDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from app.model.prompt.motivation_prompt import build_motivation_prompt
from app.model.prompt.personality_prompt import build_personality_prompt

def run_refine_chain(llm, documents, category: str):
    if category == "motivation":
        base_prompt = build_motivation_prompt("{text_chunk}")
    elif category == "personality":
        base_prompt = build_personality_prompt("{text_chunk}")
    else:
        raise ValueError("Category must be 'motivation' or 'personality'")

    initial_prompt = PromptTemplate.from_template(base_prompt)

    refine_prompt = PromptTemplate.from_template("""
Refine the existing analysis below by incorporating the new Reddit chunk provided.
Update trait ratings or personality dimensions only if new evidence suggests changes.

Existing Summary:
\"\"\"{existing_answer}\"\"\"

New Reddit Data:
\"\"\"{text_chunk}\"\"\"
""")

    chain = RefineDocumentsChain(
        initial_llm_chain=LLMChain(llm=llm, prompt=initial_prompt),
        refine_llm_chain=LLMChain(llm=llm, prompt=refine_prompt),
        document_variable_name="text_chunk",
        initial_response_name="existing_answer"
    )

    result = chain.run(documents)
    return result
