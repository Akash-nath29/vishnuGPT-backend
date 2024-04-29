import requests

while True:
    prompt = input("Enter a prompt: ")
    response = requests.post("http://127.0.0.1:80/api", json={"prompt": prompt})
    print(response.json()["response"]["completions"][0]["data"]["text"])