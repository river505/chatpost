import requests
import json
import sys

if __name__ == "__main__":
  uu,prompt=sys.argv[1],sys.argv[2]
  url = uu

  payload = json.dumps({
    "query": prompt,
    "conversation_id": "",
    "history_len": -1,

    "stream": False,
    "model_name": "Qwen-72B",
    "temperature": 0.7,
    "max_tokens": 0,
    "prompt_name": "default"
  })
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  # print("asd")
  # print(response.text)
  print(json.loads(response.text[5:])["text"])
  # print("asd")