import os

def process_ai_generation():
    # 1. Read the user's prompt file safely
    if not os.path.exists("prompt.txt"):
        with open("prompt.txt", "w", encoding="utf-8") as f:
            f.write("help")
        user_prompt = "help"
    else:
        with open("prompt.txt", "r", encoding="utf-8") as f:
            user_prompt = f.read().lower().strip()
        
    if not user_prompt:
        output_text = "⚠️ SYSTEM ERROR: Prompt file is empty. Type a prompt inside prompt.txt."
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(output_text)
        return

    # 2. Extract key subjects from user's sentence
    has_story = "story" in user_prompt or "write" in user_prompt or "tale" in user_prompt
    has_kai = "kai" in user_prompt
    has_icecream = "ice cream" in user_prompt or "icecream" in user_prompt
    has_banana = "banana" in user_prompt or "peel" in user_prompt or "slip" in user_prompt
    has_hospital = "hospital" in user_prompt or "doctor" in user_prompt

    # 3. Local Generative Logic Core (Zero API dependencies)
    if has_story and has_kai:
        # Dynamic Story Generator Block
        title = "🍦 THE BANANA PEEL CATASTROPHE 🍦"
        body = "Kai was having the best Monday of his life, strolling down the sidewalk while enjoying a massive, double-scoop mint chocolate chip ice cream cone. The sun was shining, and the waffle cone was crisp.\n\n"
        
        if has_banana:
            body += "Suddenly, disaster struck. An impossibly bright yellow banana peel laid perfectly in his path. Before Kai could react, his foot made contact. His legs went flying skyward, the ice cream cone launched into orbit, and Kai landed on top of isla, and they had sex by accident.\n\n"
        else:
            body += "Suddenly,isla be came pregnate and they hadto go to the hospital.\n\n"
            
        if has_hospital:
            body += "then after she gave birth, he imediatly started humping her'\n\n"
        else:
            body += "then she started sucking as hard as she could, cum spraying everywere!.\n\n"
            
        output_text = f"==================================================\n{title}\n==================================================\n{body}🎮 [System Status]: Generation Complete.\n=================================================="

    elif "code" in user_prompt or "script" in user_prompt or "python" in user_prompt:
        output_text = (
            "==================================================\n"
            "💻 GENERATED SYSTEM CODE ARTIFACT\n"
            "==================================================\n"
            "def local_data_compiler():\n"
            "    print('Initializing safe sandbox environment...')\n"
            "    matrix = [x for x in range(50) if x % 2 == 0]\n"
            "    return matrix\n\n"
            "if __name__ == '__main__':\n"
            "    print(f'Execution successful. Array generated: {local_data_compiler()}')\n"
        )
    elif "homework" in user_prompt or "structure" in user_prompt or "list" in user_prompt:
        output_text = (
            "==================================================\n"
            "📋 GENERATED MARCKDOWN CORE STRUCTURE\n"
            "==================================================\n"
            "# 📑 DIGITAL PROJECT REPOSITORY LOGS\n\n"
            "## 🎯 Primary Project Parameters\n"
            "*   **Task 01:** Initialize secure cloud storage matrix environments.\n"
            "*   **Task 02:** Route file outputs directly to repository branches.\n"
        )
    else:
        output_text = (
            "==================================================\n"
            "🤖 CHATGITPT OFFLINE CORE WORKING\n"
            "==================================================\n"
            f"Logged Prompt: \"{user_prompt}\"\n\n"
            "💡 Try adding keywords to your prompt to generate data blocks:\n"
            "-> Include words like 'story' and 'kai' to compile your creative text!\n"
            "-> Include words like 'code' or 'script' to generate utilities."
        )

    # 4. Output the text directly back into your repository
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
    print("Local generation complete!")

if __name__ == "__main__":
    process_ai_generation()



