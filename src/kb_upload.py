import requests
import sys
import os
uu,kb,ff=sys.argv[1],sys.argv[2],sys.argv[3]
url = uu if uu else "http://192.168.0.114:7861/knowledge_base/upload_docs"
filepath,fullflname = os.path.split(ff)
if fullflname.endswith('.pdf'):



    payload = {'to_vector_store': 'true',
    'override': 'false',
    'not_refresh_vs_cache': 'false',
    'chunk_size': '250',
    'chunk_overlap': '50',
    'zh_title_enhance': 'false',
    'knowledge_base_name': kb,
    'docs': '{\
      "test.txt": [\
        {\
          "page_content": "custom doc",\
          "metadata": {},\
          "type": "Document"\
        }\
      ]\
    }'}

    files = [
        ('files', (ff, open(ff, 'rb'),
                   'application/pdf'))
    ]
    headers = {
      'accept': 'application/json'
    }

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
