lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
precos = [2000, 9000, 6000, 11000]

dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

print(dic_produtos["airpod"])

dic_produtos["iphone"] = dic_produtos["iphone"]*1.3
print(dic_produtos)

print(len(dic_produtos))

#dic_produtos.pop("airpod")

print(dic_produtos)

dic_produtos["apple watch"] = 2500
print(dic_produtos)

#verificar item

if "Motorola" in dic_produtos:
    print("Produto existe")

#verificar valor
if 9000 in dic_produtos.values():
    print("Existe")
else:
    print("Não existe")



    nome_produto = input("Nome do produto: ")
    preco_produto = input("Valor do produto: ")

        #cadastrar produto se não existir


        #caso exista, o produto devera ser editado
    nome_produto = nome_produto.lower()
    preco_produto = float(preco_produto)

    dic_produtos[nome_produto] = preco_produto
    print(dic_produtos)


        #Alem disso o programa deve atualizar no final o preço de todos os produtos com aumento de 10%


    for produto in dic_produtos:
        novo_preco = dic_produtos[produto]*1.1
        dic_produtos[produto] = novo_preco
    print(dic_produtos)

