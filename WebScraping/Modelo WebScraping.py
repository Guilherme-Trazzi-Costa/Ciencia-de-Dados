from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

import pandas as pd

import time

chrome_driver_path = r".\chromedriver.exe"
service = Service(chrome_driver_path) 

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--window_size=1920,1080')

driver = webdriver.Chrome(service=service, options=options)

url_base = 'https://masander.github.io/AlimenticiaLTDA/#/operational'#Alterar
driver.get(url_base)

time.sleep(5)

# armazém ITENS
dic_dados = {'id_equipamento':[], 'data':[],'horas_uso':[],'turno':[]}#Alterar

try:
    WebDriverWait(driver,10).until(
        ec.presence_of_all_elements_located((By.ID, 'Table'))#Alterar
    )
    print('Elementos encontrados com sucesso!')
except TimeoutException:
    print('Tempo de espera excedido!')

linhas = driver.find_elements(By.TAG_NAME, 'tr')#Alterar

for i in linhas:
    try:
        id_equipamento = i.find_element(By.CLASS_NAME, 'td_id_equipamento').text.strip()#Alterar
        data = i.find_element(By.CLASS_NAME, 'td_data').text.strip()#Alterar
        horas_uso = i.find_element(By.CLASS_NAME, 'td_horas_uso').text.strip()#Alterar
        turno = i.find_element(By.CLASS_NAME, 'td_turno').text.strip()#Alterar
        

        dic_dados['id_equipamento'].append(id_equipamento)#Alterar
        dic_dados['data'].append(data)#Alterar
        dic_dados['horas_uso'].append(horas_uso)#Alterar
        dic_dados['turno'].append(turno)#Alterar
        
        
        print(f'{id_equipamento} - {data}')
    except Exception as e:
        print('Não foi possível coletar dados: ', e)

driver.quit()

df = pd.DataFrame(dic_dados)

df.to_excel('webscraping.xlsx', index=False)#Alterar
print('CONCLUÍDO: ', len(df))