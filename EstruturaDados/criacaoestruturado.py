# Dados estruturados - criação

#Excel

import pandas as pd
#Dicionario
dados_planilha1 = {
    "Nome": ["Ana", "Carlos", "Jessica", "Maria", "Vivian"],
    "Idade": [23, 35, 25, 34, 42],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Fortaleza"]
}

#Cria Dataframe
df_planilha1 = pd.DataFrame(dados_planilha1)

#Salvar Excel
with pd.ExcelWriter("Dados_Estruturados.xlsx") as writer:
    df_planilha1.to_excel(writer, sheet_name="Planilha1", index=False)










