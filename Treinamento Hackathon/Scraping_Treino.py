from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

import pandas as pd

import time

import re

from selenium.common.exceptions import TimeoutException


caminho_driver = "C:\chromedriver-win64\chromedriver.exe"

servico = Service(caminho_driver)
controle = webdriver.ChromeOptions()
controle.add_argument('--disable-gpu')
controle.add_argument('window-size=1920,1080')

executor = webdriver.Chrome(service=servico, options=controle)

url_site = "https://masander.github.io/AlimenticiaLTDA-financeiro/"

executor.get(url_site)

time.sleep(5)

dic_orcamento = {"Setor":[],"Mes":[], "Ano":[], "Valor_Previsto": [], "Valor_Realizado": []}
dic_despesas = {"Id_despesa":[], "Data":[], "Tipo":[], "Setor":[], "Valor":[], "Fornecedor":[]}

linha_atual = 1
pagina_atual = "Orçamento"

while True:
    print(f"\n Coletando dados da pagina {linha_atual}")

    try:

        WebDriverWait(executor,10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, ""))

        )
        print("Elementos encontrados com sucesso")
    except TimeoutException:
        print("Tempo de espera excedido")

    linhas = executor.find_elements(By.CLASS_NAME, "")

    for linha in linhas:
        try:
            #Da pra pegar a tabela completa By.xpath ...table
            setor = linha.find_element(By.CLASS_NAME, "").text.strip()
            mes = linha.find_element(By.CLASS_NAME, "").text.strip()
            ano = linha.find_element(By.CLASS_NAME, "").text.strip()
            valor_previsto = linha.find_element(By.CLASS_NAME, "").text.strip()
            valor_realizado = linha.find_element(By.CLASS_NAME, "").text.strip()

            print(f'{setor} - {mes} - {ano} - {valor_previsto} - {valor_realizado}')


            dic_orcamento["Setor"].append(setor)
            dic_orcamento["Mes"].append(mes)
            dic_orcamento["ano"].append(ano)
            dic_orcamento["Valor_Previsto"].append(valor_previsto)
            dic_orcamento["Valor_Realizado"].append(valor_realizado)

        except Exception:
            print("Erro ao coletar dados", Exception)


    try:
        botao_proximo = WebDriverWait(executor, 5).until(

            ec.element_to_be_clickable((By.XPATH, "//button[text()='Orçamentos']"))
        )
        if botao_proximo:
            executor.execute_script("arguments[0].click();", botao_proximo)
            pagina_atual = "Despesas"
            print(F"Indo para ", pagina_atual)

            time.sleep(5)

        else:
            print("Erro!")

    except Exception:
        print("Erro ao avançar para pagina", Exception)

        for linha in linhas:
            try:
                    setor = linha.find_element(By.CLASS_NAME, "").text.strip()
                    mes = linha.find_element(By.CLASS_NAME, "").text.strip()
                    ano = linha.find_element(By.CLASS_NAME, "").text.strip()
                    valor_previsto = linha.find_element(By.CLASS_NAME, "").text.strip()
                    valor_realizado = linha.find_element(By.CLASS_NAME, "").text.strip()

                    print(f'{setor} - {mes} - {ano} - {valor_previsto} - {valor_realizado}')


                    dic_despesas["Setor"].append(setor)
                    dic_despesas["Mes"].append(mes)
                    dic_despesas["ano"].append(ano)
                    dic_despesas["Valor_Previsto"].append(valor_previsto)
                    dic_despesas["Valor_Realizado"].append(valor_realizado)

            except Exception:
                print("Erro ao coletar dados", Exception)
        break
executor.quit()

df= pd.DataFrame
