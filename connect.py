import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "
}
while(1):
    input = input()
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": input }],
        "temperature": 0.7
    }


    response = requests.post(url, headers=headers, data=json.dumps(data))
    json_data = response.json()
    message = json_data['choices'][0]['message']['content']
    if response.status_code == 200:
        print(message)
    else:
        print(f"Error: {response.status_code}")
