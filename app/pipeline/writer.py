import json 
import os
def save_persona(persona_dict, output_dir = "D:\Projects\Persona_Gen\app\outputs") :
    os.makedirs(output_dir,exist_ok=True)

    # Save json 
    json_path = os.path.join(output_dir,"user_persona.json")
    with open(json_path,"w", encoding='utf-8') as f :
        json.dump(persona_dict, f, indent=4, ensure_ascii=False)


    # Save Pretty text
    txt_path = os.path.join(output_dir, "user_persona.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        for trait, value in persona_dict.items():
            f.write(f"{trait.upper()}\n")
            f.write("-" * 40 + "\n")
            if isinstance(value, list):
                for item in value:
                    f.write(f"- {item}\n")
            else:
                f.write(str(value).strip() + "\n")
            f.write("\n")
    print(f" Saved persona to:\n- {json_path}\n- {txt_path}")