import requests 

'''#Ira carregar a URL que pedimos 
url ='https://google.com'
resposta = requests.get(url)

print(resposta.text)'''
'''
# REquisição a uma API -- GET
url = 'https://api.agify.io/?name=Tiago'
resposta = requests.get(url)

dados = resposta.json()
print(dados)'''

'''
#Requiseição a uma API -- POST

url = 'https://httpbin.org/post'
dados = {'Nome':'Tiago', 'idade':25}

resposta = requests.post(url,dados)
print(resposta.json())'''

'''# Veriifcando se o site esta Online
url ='https://google.com'
resposta = requests.get(url)

if resposta.status_code == 200:
    print('Site esta online')
else:
    print('Erro ao acessar o site!')'''