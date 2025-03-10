# Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.

soma_pares = 0
soma_impares = 0
for n in range(10):
    numeros = int(input(f'Insira o {n+1}o numero: '))
    if numeros % 2 == 0:
        soma_pares += 1
    elif numeros % 2 != 0:
        soma_impares += 1
    else:
        ('Numero invalido')
print(f'A quantidade de numeros pares e: {soma_pares}')
print(f'A quantidade de numeros impares e: {soma_impares}')
