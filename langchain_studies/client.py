from langserve import RemoteRunnable

chain_remote = RemoteRunnable('http://localhost:8000/translate')
text_response = chain_remote.invoke({'language': 'inglês', 'text': 'Olá, mundo!'})
print(text_response)
