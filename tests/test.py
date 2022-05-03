import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "tweet", json={"content": "hello world!"})
print(response.json())

# curl -X POST -H "Content-Type: application/json" -d '{"content":"abc@gmail.com"}' http://127.0.0.1:5000/tweet

