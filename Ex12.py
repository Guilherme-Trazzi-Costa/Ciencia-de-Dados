# Numa eleição existem três candidatos. Faça um programa que peça o
# número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
# número de votos de cada candidato.


qtd_Eleitores = int(input('Insira a quantidade de pessoas: '))

soma_votos_A = 0
soma_votos_B = 0
soma_votos_C = 0

for n in range(0, qtd_Eleitores):
    voto = input(f'Pessoa {n+1} Insira seu voto(A/B/C): ').upper().strip()
    if voto == 'A':
        soma_votos_A += 1
    elif voto == 'B':
        soma_votos_B += 1
    elif voto == 'C':
        soma_votos_C += 1
    else:
        print('Voto invalido')
print(f'A quantidade de votos em A e: {soma_votos_A}')
print(f'A quantidade de votos em B e: {soma_votos_B}')
print(f'A quantidade de votos em C e: {soma_votos_C}')

