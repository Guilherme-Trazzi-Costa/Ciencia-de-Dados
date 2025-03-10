#Faça um programa que verifique e mostre os números entre 1.000 e 2.000

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira um numero: '))

for i in range(n1+1, n2+1):
    if i % 11 == 2:
            print(i)