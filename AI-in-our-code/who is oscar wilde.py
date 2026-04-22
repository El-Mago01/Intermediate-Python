from http.client import responses
import os
from dotenv import load_dotenv
import requests
import json
MAGO_API_KEY = os.getenv('MAGO_API_KEY')
PROJECT_NAME = "projects/250394891000"
#URL="https://api.openai.com/v1/chat/completions"
load_dotenv()
URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={MAGO_API_KEY}"

def AI_request(prompt:str) -> str:

    meta_prompt = """"
    You are supposed to create poems about a  Star-Wars character in order to do that I will give 
    you information about a character. Make it around 100 words and make it fun. There should be humour in it.  
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": "[{'role: 'user', 'content': prompt]"
    }

    headers = {
        "content-Type": "application/json",
        "Authorization": f"Bearer {MAGO_API_KEY}"
    }

    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    if response.ok:
        print(response.json())
    else:
        print("No answer was received")
        print(response)
        return response.json()
    return response.json()

def get_prompt():
    prompt=input("What is your request:")
    return prompt

def main():
    prompt=get_prompt()
    ai_answer = AI_request((prompt))
    print(ai_answer)

if __name__ == "__main__":
    main()


