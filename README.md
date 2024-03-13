## chat.sh
基本对话
参数：prompt 
```
prompt="你好"
python ./src/chat.py "http://192.168.0.114:7861/chat/chat" $prompt
```

## kb_chat.sh
知识库对话
参数：指定知识库 prompt
kb_name=""
prompt=""
python ./src/kb_upload.py "http://192.168.0.114:7861/chat/knowledge_base_chat" $prompt $kb_name

## kb_new.sh
新建知识库
参数：新知识库的名字

## kb_upload.sh
上传文件到知识库，并向量化
参数：指定知识库，本地文件地址（目前只支持pdf）
