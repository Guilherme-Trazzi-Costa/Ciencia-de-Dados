#email = input("Escreva seu email: ")
#nome = input("Seu primeiro nome: ")

#print(nome, email)

#faturamento = float(input("Escreva o faturamento: "))

#imposto = faturamento*0.1
#print(f"{imposto} R$")


vendas = [100, 50, 14, 20, 30, 700]

total_vendas = sum(vendas)

print(total_vendas)

#tamanho lista

quantidade_vendas = len(vendas)

print(quantidade_vendas)


print(max(vendas))

print(min(vendas))

lista_produtos = ["iphone", "airpod", "ipad", "macbook", "notebook"]

#produto_procurado = input("pesquise pelo nome do produto: ")
#produto_procurado = produto_procurado.lower()
#print(produto_procurado in lista_produtos)

#adicionar item
lista_produtos.append("apple watch")
print(lista_produtos)


#remover item

#lista_produtos.remove("apple watch")
#print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)


#editar item
precos = [1000, 2000, 4000]
precos[0] = 6000
print(precos)

#contar quantas vezes item aparece
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "notebook", "iphone", "iphone"]

print(lista_produtos.count("iphone"))

lista_produtos.sort()
print(lista_produtos)

vendas.sort()
print(vendas)