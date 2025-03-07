#Faça um programa que leia 5 números e informe a soma e a média dos
#números.

soma = 0
for i in range(1, 6):
  numero = int(input('Insira um numero: '))
  soma += numero
media = soma/ i
print('A soma dos numeros e: ', soma)
print('A media dos numeros e: ',media)

