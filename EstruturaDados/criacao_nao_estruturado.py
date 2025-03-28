# Dados NÃO estruturados - criação

#CSV

import pandas as pd
#Dicionario
dados_csv = {
    "Nome": ["Ana", "Carlos", "Jessica", "Maria", "Vivian"],
    "Idade": [23, 35, 25, 34, 42],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza"]
}

#criar dataframe
df_csv = pd.DataFrame(dados_csv)

#Salvar em csv
df_csv.to_csv("Dados_Nao_Estruturados.csv", index=False)