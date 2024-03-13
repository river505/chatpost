import requests
import json
import sys
uu,asd = sys.argv[1],sys.argv[2]
url = uu if uu else "http://192.168.0.114:7861/knowledge_base/create_knowledge_base"

payload = json.dumps({
  "knowledge_base_name": asd,
  "vector_store_type": "faiss",
  "embed_model": "bge-large-zh-v1.5"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
