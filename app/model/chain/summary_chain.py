# models/chains/summary_chain.py

from langchain.chains import MapReduceDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from model.prompt.description_prompt import build_description_prompt

def run_summary_chain(llm, documents, category: str):
    map_prompt = PromptTemplate.from_template(
        build_description_prompt("{text_chunk}", category)
    )
    map_chain = LLMChain(llm=llm, prompt=map_prompt)

    reduce_prompt = PromptTemplate.from_template("""
Given these extracted points and their evidences from multiple Reddit posts, summarize the key {category} traits into 3–5 bullet points with justifications.

{input}
""")
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

    chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        reduce_chain=reduce_chain,
        document_variable_name="text_chunk",
        return_intermediate_steps=False,
    )

    result = chain.run(documents)
    return result
