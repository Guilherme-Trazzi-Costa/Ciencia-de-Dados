import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL do site a ser acessado
url = 'http://books.toscrape.com/'

#Fazer requisição HTTP 
response = requests.get(url)

#criar objeto BeautifulSoup para analisar HTML
soup = BeautifulSoup(response.text, 'html.parser')

#Criar uma lista para armazenar os dados
books_data = []

#Encontrar elementos que contém a tag article com classe product_pod
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a.attrs['title']
    price = book.find('p', class_='price_color').text
    books_data.append([title, price])

df = pd.DataFrame(books_data, columns=['Titulo', 'Preço'])

df.to_excel('livros.xlsx', index=False)

print('Dados Salvos no Arquivo livros.xlsx com sucesso !')






