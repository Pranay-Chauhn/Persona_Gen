from app.model.chain.runner import run_chain_for_trait

def run_persona_extraction(llm, documents):
    """
    Runs the full pipeline and returns a structured user persona dict.
    """
    trait_groups = [
        "Name",
        "Age",
        "Occupation",
        "4 Words",
        "Habits",
        "Goals",
        "Frustrations",
        "Motivations",
        "Personality"
    ]

    print(" Starting persona extraction...")
    persona_result = {}

    for trait in trait_groups:
        print(f" Extracting: {trait}")
        output = run_chain_for_trait(llm, documents, trait)

        persona_result[output['trait']] = output['result']

    print(" Persona extraction completed.")
    return persona_result
