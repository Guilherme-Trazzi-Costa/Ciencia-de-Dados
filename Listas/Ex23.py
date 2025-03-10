lista = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

soma = 0
contador = 0
for n in lista:
    contador += 1
    soma += n

media = soma/contador

print(f' A soma dos numeros e: {soma}')
print(f'A quantidade de numeros e: {contador}')
print(f'A media e: {media}')
