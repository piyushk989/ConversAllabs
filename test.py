import requests

response = requests.post(
    "http://localhost:8000/create-agent",
    json={
        "provider": "vapi",
        "name": "Test",
        "model": "gpt-3.5-turbo",
        "voice": "1",
        "prompt": "Hello"
    }
)
print(response.status_code, response.json())
