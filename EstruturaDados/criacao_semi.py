# Dados semi estruturados - criação

#JSON

import pandas as pd
#Dicionario
dados_json = {
    "Nome": ["Ana", "Carlos", "Jessica", "Maria", "Vivian"],
    "Idade": [23, 35, 25, 34, 42],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza"]
}

#Criar Dataframe
df_json = pd.DataFrame(dados_json)

print(df_json)

#Salvar em Json

df_json.to_json("Dados_Semi.json", orient= "records", lines= False)