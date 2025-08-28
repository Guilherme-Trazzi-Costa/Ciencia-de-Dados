# Imports
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

emuladorChrome = "C:\chromedriver-win64\chromedriver.exe"


# Configaração do WebDriver
servico = Service(emuladorChrome)
controle = webdriver.ChromeOptions()
controle.add_argument('--disable-gpu')
controle.add_argument('--window-size=1920,1080')

# Inicializador do WebDriver
executador = webdriver.Chrome(service = servico, options = controle)

# URL Inicial
url_site = 'https://www.ruacep.com.br/sp/municipios/'
executador.get(url_site)
time.sleep(5)

# Dicionário para inserir os CEPs
dic_CEP = {
    'CEP': []
}

# Contador de pág
pag = 1

# Coleta os dados
while True:
    print(f'\n Coletando dados da página {pag}...')
    try:
        WebDriverWait(executador, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'card'))
        )
        print('Elementos encontrados com sucesso!')
    except TimeoutException:
        print('Tempo de espera excedido')

    ceps = executador.find_elements(By.CLASS_NAME, 'card')

    for cep in ceps:
        try:
            cep_corpo = cep.find_element(By.CLASS_NAME, 'card-body')
            p = cep_corpo.find_element(By.CLASS_NAME, 'card-text')
            texto = p.text.strip()

            match = re.search(r'CEP:\s*([\d\-]+ à [\d\-]+)', texto)
            if match:
                faixa_cep = match.group(1)
                dic_CEP['CEP'].append(faixa_cep)
                print("CEP:", faixa_cep)
            else:
                print("CEP não encontrado no texto:", texto)

        except Exception as e:
            print('Erro ao coletar dados:', e)
    try:
        btn_prox = WebDriverWait(executador, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'page-link'))
        )
        if btn_prox:
            executador.execute_script('arguments[0].scrollIntoView();', btn_prox)
            time.sleep(5)
            executador.execute_script('arguments[0].click();', btn_prox)
            print(f'Indo para a página {pag}')
            pag += 1
            time.sleep(5)
        else:
            print('Você chegou na última página!')
            break
    except Exception as e:
        print('Erro ao tentar avançar para a próxima página.', e)
        break

executador.quit()

df = pd.DataFrame(dic_CEP)
df.to_excel('CEP_dos_municipios.xlsx', index=False)
print(f'Arquivo gerado com sucesso, {len(df)} CEPs encontrados')