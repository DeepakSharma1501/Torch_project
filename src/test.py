import os
import requests
from dotenv import load_dotenv

# 1. Load the hidden variables from your local .env file
load_dotenv()

# 2. Extract your key using the os module
api_key = os.environ.get("GEMINI_API_KEY")

# 3. CRITICAL FIX: The key MUST be appended to the end of the URL via '?key='
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

# Set the standard JSON content type header
headers = {"Content-Type": "application/json"}

# The exact nested JSON payload required by Google's API servers
payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "What is a neural network in one sentence?"
                }
            ]
        }
    ]
}

try:
    # Send the raw HTTPS POST network bundle across the web
    response = requests.post(url, headers=headers, json=payload)
    
    # Catch any bad HTTP statuses (like 400, 403, 404, 500) before parsing data
    response.raise_for_status()
    
    # Convert the raw incoming byte text into a standard Python dictionary
    data = response.json()
    
    # 4. FIX: Access the deeply nested text object accurately using list index integers [0]
    ai_response_text = data['candidates'][0]['content']['parts'][0]['text']
    
    print("🤖 Response from Gemini:")
    print(ai_response_text)

except requests.exceptions.HTTPError as http_err:
    print(f"❌ HTTP Error Occurred: {http_err}")
    print(f"📄 Raw Server Error Body: {response.text}")
except KeyError:
    print("❌ Failed to parse data. Google returned a successful 200 code, but with an unexpected layout:")
    print(response.json())
except Exception as err:
    print(f"❌ An unexpected error occurred: {err}")
