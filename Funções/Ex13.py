lista = [6, 2, 3, 5, 15, 7, 9]

def multiplos3(lista):
    quantidade3 = 0
    for n in lista:
        if n % 3 ==0:
            quantidade3 += 1
    return quantidade3 
print(multiplos3(lista))