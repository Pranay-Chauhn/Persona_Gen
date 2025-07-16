# models/chains/runner.py

from app.model.chain.fact_chain import run_fact_chain
from app.model.chain.summary_chain import run_summary_chain
from app.model.chain.refine_chain import run_refine_chain

def run_chain_for_trait(llm, documents, trait_name: str):
    trait_name_lower = trait_name.lower()

    # ---------------------
    #  FACT TRAITS
    # ---------------------
    if trait_name_lower in ["name", "age", "occupation", "status", "location","tier", "Archetype"]:
        print(f"Running fact chain for {trait_name}")
        result = run_fact_chain(llm, documents, trait_name)
        return {
            "trait": trait_name,
            "result": result
        }

    # ---------------------
    #  SUMMARY TRAITS
    # ---------------------
    elif trait_name_lower in ["4-words", "Behavior and Habits", "Goals and Needs", "Frustrations"]:
        print(f" Running summary chain for {trait_name}")
        result = run_summary_chain(llm, documents, trait_name)
        return {
            "trait": trait_name,
            "result": result
        }

    # ---------------------
    #  REFINED TRAITS
    # ---------------------
    elif trait_name_lower in ["motivation", "personality"]:
        print(f" Running refine chain for {trait_name}")
        result = run_refine_chain(llm, documents, trait_name_lower)
        return {
            "trait": trait_name,
            "result": result
        }

    else:
        raise ValueError(f" Unknown trait name: {trait_name}")
