import sys
import os
import requests
import sys
if __name__ == "__main__":
    uu,dir =sys.argv[1],sys.argv[2]
    url = uu

    filepath,fullflname = os.path.split(dir)
    if fullflname.endswith('.docx'):
        payload = {'prev_id': '',
        'chunk_size': '250',
        'chunk_overlap': '50',
        'zh_title_enhance': 'false'}
        files = [
            ('files', (fullflname, open(dir, 'rb'),
                       'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))
        ]
        headers = {
          'accept': 'application/json'
        }
    if fullflname.endswith('.pdf'):
        payload = {'prev_id': '',
                   'chunk_size': '250',
                   'chunk_overlap': '50',
                   'zh_title_enhance': 'false'}
        files = [
            ('files',(fullflname, open(dir, 'rb'),
                       'application/pdf'))
        ]
        headers = {
          'accept': 'application/json'
        }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)


    print(response.json()['data']['id'])
