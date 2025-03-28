#Estruturado
#Excel

import pandas as pd

df_excel = pd.read_excel("Dados_Estruturados.xlsx", sheet_name=["Planilha1"])
print(df_excel)