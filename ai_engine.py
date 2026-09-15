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

    print(f"Executing prompt: '{user_prompt}' via cloud model server...")

    # 2. Route directly to an open-source model inference endpoint
    # Using an open API endpoint ensures zero key management requirements for your account
    API_URL = "https://huggingface.co"
    
    payload = {
        "inputs": f"<|system|>\nYou are an advanced, helpful AI assistant. Answer the user's question perfectly.</s>\n<|user|>\n{user_prompt}</s>\n<|assistant|>\n",
        "parameters": {"max_new_tokens": 500, "temperature": 0.7}
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        output_data = response.json()
        
        # Parse text generation output fields cleanly
        if isinstance(output_data, list) and "generated_text" in output_data[0]:
            full_text = output_data[0]["generated_text"]
            # Clean up model syntax tokens from final display string
            ai_response = full_text.split("<|assistant|>\n")[-1].strip()
        else:
            ai_response = f"⚠️ Server Busy or Rate Limited. Raw response: {str(output_data)}"
            
    except Exception as e:
        ai_response = f"❌ Local Execution Error: {str(e)}"

    # 3. Output the exact AI answer back to output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ai_response)
    print("Generation complete!")

if __name__ == "__main__":
    process_ai_generation()

    
    print("Generation complete!")

if __name__ == "__main__":
    process_ai_generation()

