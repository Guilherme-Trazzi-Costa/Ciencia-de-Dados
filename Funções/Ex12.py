lista = [-1, 2, -3, 5, -5, 7, -9]

def positivos(lista):
    quantidadepositivos = 0
    for n in lista:
        if n > 0:
            quantidadepositivos += 1
    return quantidadepositivos 
print(positivos(lista))
