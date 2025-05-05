from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException
import re


chrome_driver_path =  "C:\chromedriver-win64\chromedriver.exe"

servico = Service(chrome_driver_path)
controle = webdriver.ChromeOptions()
controle.add_argument('--disable gpu')
controle.add_argument('--window-size=1920,1080')

executor = webdriver.Chrome(service=servico, options=controle)

url = 'https://www.imdb.com/pt/chart/top/'

executor.get(url)
time.sleep(5)

dic_filmes = {'Titulo':[], 'Classificacao':[], 'Ano':[]}
pagina = 1
filmes = 0

while True:
    print(f"\Coletando dados da página {pagina}")

    try:
        WebDriverWait(executor, 15).until(
        ec.presence_of_all_elements_located((By.CLASS_NAME, 'ipc-metadata-list-summary-item__c'))
    )
        
    except TimeoutException as e:
        print("Não encontrado", e)

    catalogo = executor.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item__c')
    print(f"Título do filme ")

    for filme in catalogo:
        filmes += 1
        try:
            titulo = filme.find_element(By.CLASS_NAME, 'ipc-title__text').text.strip()
            classificacao = filme.find_element(By.CLASS_NAME, 'cli-title-metadata').text.strip()
            ano = filme.find_element(By.CLASS_NAME, 'cli-title-metadata-item').text.strip()


            #classificacao1 = classificacao[11:].split()

        
            classificacao1 = re.search(r'(Livre)|(10)|(12)|(14)|(16)|(18)', classificacao, re.IGNORECASE)

            classificacao1 = classificacao1.group(0) if classificacao1 else 'Não encontrada'
            

            dic_filmes['Titulo'].append(titulo)
            dic_filmes['Classificacao'].append(classificacao1)
            dic_filmes['Ano'].append(ano)

            print(f'{titulo} - {classificacao1} - {ano}')

        except Exception as e:
            print('Dados não coletados')   
    print("Coleta finalizada")
        

    executor.quit()

    df = pd.DataFrame(dic_filmes)
    df.to_excel("Filmes.xlsx", index = False)
    print(f'Arquivo salvo!')
    


        


    







