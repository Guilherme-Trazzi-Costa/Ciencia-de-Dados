lista_precos = [1500, 1000, 800, 3000]

#Imposto
#aliquota1 - IR = 0.2 se o preço for até 2000 acima disso é 0.3
#aliquota2 - ISS = 0.15
#aliquota3 - CSLL = 0.05

def calculo_imposto(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco 
    imposto_ir = 0.2 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total


for preco in lista_precos:
    imposto_total = calculo_imposto(preco)
    print(f"Imposto total sobre o produto de R${preco}: R${imposto_total}")


nova_lista = [3000, 5000, 6000, 7000]

for preco in nova_lista:
    imposto_total = calculo_imposto(preco)
    print(f"Imposto total sobre o produto de R${preco}: R${imposto_total}")
