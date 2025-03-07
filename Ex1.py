#Faça um programa que leia 5 números e informe o maior número.

n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))
n4 = int(input('Insira o quarto numero: '))
n5 = int(input('Insira o quinto numero: '))

numeros = [n1, n2, n3, n4, n5]

# for i in numeros:
#     for i in numeros:       
print('O maior numero e: ', max(numeros))
