# Faça um programa que peça para n pessoas a sua idade, ao final o
# programa deverá verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.


soma_idades = 0

qtd_pessoas = int(input('Insira a quantidade de pessoas: '))

for n in range(0, qtd_pessoas):
    idade = int(input(f'Insira a idade da pessoa {n+1}: '))
    soma_idades += idade
media = soma_idades / n
if media > 0 and media <= 25:
    print('A media de pessoas e jovem')
elif media > 25 and media <= 60:
    print('A media de pessoas e adulta')
else:
    print('A media de idades e idosa')
