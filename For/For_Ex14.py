# Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

nota = float(input('Insira uma nota: '))

for n in range(0, 2):
    if nota < 0 or nota > 10:
        nota = float(input('Insira uma nota valida: '))
    else:
        print('Nota Valida !')
        

