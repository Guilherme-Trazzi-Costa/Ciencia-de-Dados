#Faça um programa que receba um número e usando laços de repetição
#calcule e mostre a tabuada desse número.

numero = int(input("Entre com um numero: "))

for i in range(1, 11):
  print(f'{i} X {numero} = {i*numero}')