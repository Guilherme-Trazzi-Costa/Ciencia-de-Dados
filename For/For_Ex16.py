#Faça um programa que receba a idade de 15 pessoas e que calcule e
#mostre:

soma_idades = 0
idade_15 = 0
idade_30 = 0
idade_45 = 0
idade_60 = 0
idade_61 = 0


for n in range(0, 15):
    idade = int(input(f'Insira a idade da pessoa {n+1}: '))
    soma_idades += idade
    if idade <= 15:
        idade_15 += 1
    elif idade > 16 and idade <= 30:
        idade_30 += 1
    elif idade > 31 and idade <= 45:
        idade_45 += 1
    elif idade > 46 and idade <= 60:
        idade_60 += 1
    elif idade > 61:
        idade_61 += 1

percentual_15 = (idade_15/15)*100

percentual_61 = (idade_61/15)*100


print('Pessoas na faixa etaria ate 15: ', idade_15)
print('Pessoas na faixa etaria entre 16 e 30: ', idade_30)
print('Pessoas na faixa etaria entre 31 e 45: ', idade_45)
print('Pessoas na faixa etaria entre 46 e 60: ', idade_60)
print('Pessoas na faixa etaria acima de 61: ', idade_61)

print(f'A relacao de pessoa na faixa etaria ate 15 e de: {percentual_15:.2f}%' )

print(f'A relacao de pessoa na faixa etaria acima de 61: {percentual_61:.2f}%' )