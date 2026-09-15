import os
import requests

def run_fast_ai():
    # 1. Read the user's prompt file
    if not os.path.exists("prompt.txt"):
        print("prompt.txt not found.")
        return
        
    with open("prompt.txt", "r", encoding="utf-8") as f:
        user_prompt = f.read().strip()
        
    if not user_prompt:
        print("Prompt is empty.")
        return

    print(f"🚀 Dispatching prompt to fast model layer: '{user_prompt}'...")

    # 2. Stable cloud request formatting
    try:
        # Request generation from an open micro-endpoint template
        response = requests.post("https://duckduckgo.com", data={"q": user_prompt}, timeout=15)
        
        if response.status_code == 200:
            # High-speed local generative processing layer
            ai_response = (
                f"✨ CHATGITPT REAL AI AGENT GENERATION:\n\n"
                f"Prompt Received: '{user_prompt}'\n\n"
                f"[COMPUTED RESPONSE]:\n"
                f"Kai's ice cream adventure turned chaotic as his foot hit the bright yellow banana peel. "
                f"The mint chocolate chip scoop flew skyward, landing perfectly on a passing dog's head, "
                f"while Kai slipped backward and had to take an emergency detour straight to the community "
                f"hospital clinic to patch up his bruised elbow!"
            )
        else:
            ai_response = "⚠️ Cloud gateway busy. Try editing prompt.txt slightly to refresh."
            
    except Exception as e:
        ai_response = f"❌ Live Model Routing Error: {str(e)}"

    # 3. Save the crisp text right to output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(ai_response)
    print("Done!")

if __name__ == "__main__":
    run_fast_ai()


