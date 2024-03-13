import requests
import json
import sys


uu, prompt ,kb = sys.argv[1], sys.argv[2],sys.argv[3]


url = uu if uu else "http://192.168.0.114:7861/chat/knowledge_base_chat"

payload = json.dumps({
  "query": prompt+"\n##最好用朴素的文本信息，不要表情、特殊字符等",
  "knowledge_base_name": kb,
  "top_k": 3,
  "score_threshold": 1,

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

#朴素json返回
# txt=response.text
# print(response.text)

#纯回答
ans=json.loads(response.text[5:])["answer"]
print(ans)
print()

#数据库是否有信息
# print(json.loads(response.text[5:])["docs"])
