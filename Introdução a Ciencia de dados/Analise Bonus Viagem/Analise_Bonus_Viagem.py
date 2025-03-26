import pandas as pd
import openpyxl as ex
import twilio as tw


#Abrir 6 arquivos em excel

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]


for mes in lista_meses:

    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
# Para cada arquivo:

#  Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]

        print(f"No mês {mes}, o vendedor {vendedor}, bateu a meta e vendeu {vendas}")




#Se valor maior que 55.000, madar sms para o celular com nome mes e valor de venda do vendedor





#Caso não seja maior que 55.00 não fazer nada




