import os
from transformers import pipeline

def run_real_ai():
    # 1. Read whatever the user typed
    if not os.path.exists("prompt.txt"):
        print("prompt.txt not found.")
        return
        
    with open("prompt.txt", "r", encoding="utf-8") as f:
        user_prompt = f.read().strip()
        
    if not user_prompt:
        print("Prompt is empty.")
        return

    print(f"🤖 Loading Neural Network into memory to process: '{user_prompt}'...")

    try:
        # 2. Initialize a true, self-contained text generation AI model
        # This runs 100% locally on the GitHub server machine—no APIs, no network blocks.
        generator = pipeline("text-generation", model="gpt2")
        
        # 3. Compute and generate original text tokens
        print("🧠 Computing token weights and generating response...")
        results = generator(
            user_prompt, 
            max_length=150, 
            num_return_sequences=1,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )
        
        ai_response = results[0]["generated_text"]
        
    except Exception as e:
        ai_response = f"❌ Machine Learning Engine Error: {str(e)}"

    # 4. Save the machine-generated text to output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ai_response)
    print("🤖 Generation complete! Output saved.")

if __name__ == "__main__":
    run_real_ai()



