import os
import requests

def process_ai_generation():
    # 1. Read the user's prompt file
    if not os.path.exists("prompt.txt"):
        print("Error: prompt.txt file not found.")
        return
        
    with open("prompt.txt", "r", encoding="utf-8") as f:
        user_prompt = f.read().strip()
        
    if not user_prompt:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write("⚠️ SYSTEM ERROR: Prompt file is empty. Type a question inside prompt.txt.")
        return

    print(f"Executing prompt: '{user_prompt}' via high-capacity endpoint...")

    # 2. Ultra-stable open endpoint setup
    API_URL = "https://openrouter.ai"
    
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant. Answer the user's prompt beautifully."},
            {"role": "user", "content": user_prompt}
        ]
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        
        # Check if we got a valid JSON object back
        if response.status_code == 200:
            output_data = response.json()
            if "choices" in output_data and len(output_data["choices"]) > 0:
                ai_response = output_data["choices"][0]["message"]["content"].strip()
            else:
                ai_response = f"⚠️ Server structure error. Raw output: {str(output_data)}"
        else:
            ai_response = f"⚠️ Server returned status code {response.status_code}. Retrying..."
            
    except Exception as e:
        ai_response = f"❌ Local Engine Runtime Error: {str(e)}"

    # 3. Output the exact AI answer back to output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ai_response)
    print("Generation process complete!")

if __name__ == "__main__":
    process_ai_generation()


