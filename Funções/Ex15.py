lista = [-1, 2, -3, 5, -5, 7, -9]

def subspor0(lista):
    for n in range(len(lista)):
        if lista[n] < 0:
            lista[n] = 0
    return lista
print(subspor0(lista))