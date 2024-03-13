import requests

url = "http://localhost:7862/knowledge_base/upload_temp_docs"

payload = {'prev_id': '',
'chunk_size': '250',
'chunk_overlap': '50',
'zh_title_enhance': 'false'}
files=[
  ('files',('3月工作日志.docx',open('C:/Users/user/Desktop/3月工作日志.docx','rb'),'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))
]
headers = {
  'accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)