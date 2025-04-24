#Módulo para controlar navegador
from selenium import webdriver

#Localizador de elementos
from selenium.webdriver.common.by import By

#Serviço para configurar caminho do executavel chrome driver
from selenium.webdriver.chrome.service import Service

#Classe que permite executar ações avançadas(mover mouse, clicar e arrastar etc)
from selenium.webdriver.common.action_chains import ActionChains

#Classe que espera de forma explicita até que a condição seja satisfeita(elemento aparecer)
from selenium.webdriver.support.ui import WebDriverWait

#Condições esperadas usadas com WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Trabalhar com dataframe
import pandas as pd

#Funções de tempo
import time

#Tratamento de excessão
from selenium.common.exceptions import TimeoutException


#Definir caminho do WebDriver
caminho_driver = "C:\chromedriver-win64\chromedriver.exe"


#Configuração WebDriver
servico = Service(caminho_driver) #Navegador controlado pelo selenium
controle = webdriver.ChromeOptions() #Configurar opções do navegador
#controle.add_argument('--headless') #Executa o chrome sem abrir interface visual
controle.add_argument('--disable-gpu') #Evita possíveis erros gráficos
controle.add_argument('--window-size=1920,1080')# Define resolução fixa de tela

#Inicialização do WebDriver
executador = webdriver.Chrome(service=servico, options=controle)

# URL inicial
url_site = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

executador.get(url_site)

time.sleep(5) #aguarda 5 segundos para garantir que a pagina carregue

#criar dicionário vazio para armazenar nomes e preços das cadeiras
dic_produtos = {'Titulo':[], 'Preco':[]}

#Vamos iniciar na pagina 1 e ir incrementando em cada troca de pagina
pagina_atual = 1

while True:
    print(f'\n Coletando dados da pagina {pagina_atual}...')
    
    try:
    
        #webdriverwait cria uma espera de até 10 seg
        #until faz com que o código espere até qiue a condição seja verdadeira
        #ec.resence_of_all_elements_located verifica se todos os elemnetos 'productcard' estão acessiveis
        #By.Class indica que a busca será feita através da classe CSS de valor 'productcard'

        WebDriverWait(executador, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'productCard'))
        )
        print('Elementos encontrados com sucesso')
    except TimeoutException:
        print('Tempo de espera excedido')

    produtos = executador.find_elements(By.CLASS_NAME, 'productCard')

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, 'nameCard').text.strip()
            preco = produto.find_element(By.CLASS_NAME, 'priceCard').text.strip()

            print(f'{nome} - {preco}')

            dic_produtos['Titulo'].append(nome)
            dic_produtos['Preco'].append(preco)

        except Exception:
            print('Erro ao coletar dados:', Exception)

#Encontrar acesso para prox pagina 
    try:
        botao_proximo = WebDriverWait(executador, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, 'nextLink'))
    #Encontrar elemento
        )
        if botao_proximo:
            executador.execute_script('arguments[0].scrollIntoView();', botao_proximo)
            time.sleep(1)

        #Clicar no botão
            executador.execute_script('arguments[0].click();', botao_proximo)
            pagina_atual += 1
            print(f'Indo para a pagina {pagina_atual}')
            
            time.sleep(5)

        else:
            print('Última página')
    
    except Exception:
        print('Erro ao avnaçar para próxima página', Exception)
        break

#Fecha navegador
executador.quit()

#Criar dataframe para tratar os dados
df = pd.DataFrame(dic_produtos)

#Salvar dados em csv a partir do dataframe
df.to_excel("Cadeiras.xlsx", index = False)

print(f'Arquivo salvo com sucesso! ({len(df)} produtos armazenados)')














