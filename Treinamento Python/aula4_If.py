vendas = 1500
meta1 = 1800 #10% bonus
meta2 = 1500 #5% bonus

if vendas >= meta1:
    print("vendedor ganhya bônus")
    print("Bateu a meta de vendas")
    bonus = 0.1*vendas
    print("Bônus do vendedor: ", bonus)

else:
    print("Vendedor não bateu meta")
    print("Vendedor não Ganhará Bônus")


    #Segundo Cenário

vendas = 1500
meta1 = 1800 #10% bonus
meta2 = 1500 #5% bonus

if vendas >= meta1:
    bonus = 0.1*vendas
elif vendas >= meta2:
        bonus = 0.05*vendas
else:
        bonus = 0

print("Bônus: ", bonus)


lista = ["airpod", "macbook", "iphone", "ipod"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista:
      print("produto no estoque")
else:
      print("Não temos esse produto")
