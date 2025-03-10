lista = [6, 2, 3, 5, 18, 7, 9]

def soma_lista(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma

print(soma_lista(lista))

