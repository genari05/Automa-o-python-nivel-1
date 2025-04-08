#BeautifulSoup apenas mexe na estrutura HTML

from bs4 import BeautifulSoup

html = '''
    <html>
        <body>
            <h1>Ola mundo</h1>
            <p class="mensagem">Bem-vindo ao web scraping</p>
            <p class="teste">Outro teste</p>
        </body>
    </html>
'''
soup = BeautifulSoup(html,'html.parser')
print(soup.h1.text)# Saida: Ola mundo 
print(soup.p.text)# Saida:Bem vindo...