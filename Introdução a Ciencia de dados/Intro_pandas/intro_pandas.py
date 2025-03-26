import pandas as pd

vendas_df = pd.read_excel("Vendas.xlsx")
#print(vendas_df.describe())

#produtos = vendas_df["Produto"]
#print(produtos)

print(vendas_df.loc[1:5])

vendas_df["Comissão"] = vendas_df["Valor Final"]*0.1
print(vendas_df)