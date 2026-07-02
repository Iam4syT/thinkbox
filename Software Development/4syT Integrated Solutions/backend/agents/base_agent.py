import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        # Check for Groq API key first, then fallback to OpenAI API key
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, query):
        if self.groq_api_key:
            # Use Groq API
            try:
                headers = {
                    "Authorization": f"Bearer {self.groq_api_key}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "llama3-8b-8192",
                    "messages": [
                        {"role": "system", "content": f"You are {self.name}, {self.description}. Respond in a helpful, concise, and professional manner."},
                        {"role": "user", "content": query}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 600
                }
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=10
                )
                if response.status_code == 200:
                    return response.json()["choices"][0]["message"]["content"]
                else:
                    return f"Error (Groq): {response.status_code} - {response.text}"
            except Exception as e:
                return f"An error occurred calling Groq: {str(e)}"
        elif self.openai_api_key:
            # Use OpenAI API
            try:
                headers = {
                    "Authorization": f"Bearer {self.openai_api_key}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": f"You are {self.name}, {self.description}. Respond in a helpful, concise, and professional manner."},
                        {"role": "user", "content": query}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 600
                }
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=10
                )
                if response.status_code == 200:
                    return response.json()["choices"][0]["message"]["content"]
                else:
                    return f"Error (OpenAI): {response.status_code} - {response.text}"
            except Exception as e:
                return f"An error occurred calling OpenAI: {str(e)}"
        else:
            return "Error: No API keys configured. Please set GROQ_API_KEY or OPENAI_API_KEY in your .env file."
