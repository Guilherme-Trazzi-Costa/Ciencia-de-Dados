import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

nome_pasta_selecionada = askdirectory()

print(nome_pasta_selecionada)

lista_arquivos = os.listdir(nome_pasta_selecionada)

nome_pasta_backup = "backup"
nome_completo_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"
if not os.path.exists(nome_completo_backup):
    os.mkdir(nome_completo_backup)

data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")

for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_backup}/{data_atual}/{arquivo}"

    if not os.path.exists(f"{nome_completo_backup}/{data_atual}"):
        os.mkdir(f"{nome_completo_backup}/{data_atual}")

    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif "backup" != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)


