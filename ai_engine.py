import os

def process_ai_generation():
    # 1. Read the user's prompt file
    if not os.path.exists("prompt.txt"):
        print("Error: prompt.txt file not found.")
        with open("prompt.txt", "w", encoding="utf-8") as f:
            f.write("help")
        user_prompt = "help"
    else:
        with open("prompt.txt", "r", encoding="utf-8") as f:
            user_prompt = f.read().lower().strip()
        
    if not user_prompt:
        output_text = "⚠️ SYSTEM ERROR: Prompt file is empty. Type a command inside prompt.txt."
    
    # 2. Local Generative Architecture Matrix (Token Core Engine)
    elif "code" in user_prompt or "script" in user_prompt or "python" in user_prompt:
        output_text = (
            "==================================================\n"
            "💻 GENERATED CODE ARTIFACT\n"
            "==================================================\n"
            "def custom_matrix_processor():\n"
            "    \"\"\"\n"
            "    Generated clean processing architecture template.\n"
            "    \"\"\"\n"
            "    print('Initializing local pipeline processes...')\n"
            "    data_matrix = [x for x in range(100) if x % 2 == 0]\n"
            "    return data_matrix\n\n"
            "if __name__ == '__main__':\n"
            "    result = custom_matrix_processor()\n"
            "    print(f'Execution successful. Sequence length: {len(result)}')\n"
        )
    elif "structure" in user_prompt or "list" in user_prompt or "organize" in user_prompt:
        output_text = (
            "==================================================\n"
            "📋 GENERATED MARKDOWN CORE STRUCTURE\n"
            "==================================================\n"
            "# 📑 DETAILED CONFIGURATION DASHBOARD\n\n"
            "## 🎯 Primary Operational Targets\n"
            "*   **Objective 01:** Implement a resilient code infrastructure matrix.\n"
            "*   **Objective 02:** Optimize local file extraction logic structures.\n"
            "*   **Objective 03:** Enforce strict local environment data isolation.\n\n"
            "## 🛠️ Associated Operational Presets\n"
            "1. Setup environment path nodes\n"
            "2. Initialize execution scripts\n"
            "3. Verify local repository outputs\n"
        )
    elif "help" in user_prompt or "info" in user_prompt:
        output_text = (
            "==================================================\n"
            "ℹ️ LOCAL ENGINE COMMAND SCHEMA SYSTEM\n"
            "==================================================\n"
            "Type your command into 'prompt.txt' and commit changes.\n"
            "Supported keyword triggers:\n"
            "➡️ 'code'      : Generates functional programming scripts\n"
            "➡️ 'structure' : Generates formatted scannable templates\n"
            "➡️ 'help'      : Shows this interaction menu matrix\n"
        )
    else:
        output_text = (
            "==================================================\n"
            "📝 TERMINAL MATRIX GENERATION OUTCOME\n"
            "==================================================\n"
            f"Parsed Prompt String Logged: \"{user_prompt}\"\n\n"
            "💡 [Local Advice]: No major execution token triggered.\n"
            "Try adding keywords like 'code' or 'structure' to prompt.txt."
        )

    # 3. Output the text directly back into your repository
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
    print("Generation complete!")

if __name__ == "__main__":
    process_ai_generation()
