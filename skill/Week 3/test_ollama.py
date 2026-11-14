import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Explain Artificial Intelligence in simple words.",
    "stream": False
}

response = requests.post(url, json=data)

result = response.json()

print("Ollama Response:")
print(result["response"])