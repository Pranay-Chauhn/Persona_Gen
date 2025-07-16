from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from app.model.prompt.fact_prompt import build_fact_prompt

def run_fact_chain(llm, chunks, trait: str):
    results = []

    for chunk in chunks:
        prompt_str = build_fact_prompt(chunk.page_content, trait)
        prompt = PromptTemplate.from_template("{input}")
        chain = LLMChain(llm=llm, prompt=prompt)
        
        response = chain.run(input=prompt_str)
        results.append(response)

    # You can add post-processing here to filter Not Found, pick top evidence, etc.
    return results