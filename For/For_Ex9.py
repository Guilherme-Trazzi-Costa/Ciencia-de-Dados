#Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1

numero = int(input('Insira um numero: '))
contador = 0
if numero < 2:
    print('Nao e Primo')
else:
    for i in range(2, numero+1):
        if numero % i == 0:
            contador += 1
if contador >= 1:
    print('Nao Primo')
else: 
    print('Primo')