#Classifique as temperaturas

#menor que 15 graus - muito frio
#entre 15 e 20 graus - frio
#entre 20 e 26 graus - agradavel
#acima de 26 - quente

temperatura = int(input('Insira a temperatura: '))

if temperatura < 15:
  print('muito frio')
elif temperatura <= 20:
  print('frio')
elif  temperatura <= 26:
  print('Agradavel')
else:
  print('quente')

#1-Escreva um programa que leia a nota de um aluno (de 0 a 100)

nota = float(input('Insira a nota: '))

if nota >= 90:
  print('Conceito A')
elif nota >= 80 and nota < 90:
  print('Conceito B')
elif  nota >= 70 and nota < 80:
  print('Conceito C')
elif  nota >= 60 and nota < 70:
  print('Conceito C')
else:
  print('Conceito D')

#2-Crie um programa que leia a idade de uma pessoa e imprima:

idade = int(input('Insira a idade: '))

if idade <= 12:
  print('Criança')
elif idade > 12 and idade <= 17:
  print('Adolescente')
elif idade >= 18 and idade <= 64:
  print('Adulto')
else:
  print('Idoso')

#3-Desenvolva um programa que calcule o IMC

peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura:'))

imc = peso / (altura**2)

if imc < 18.5:
  print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
  print('Peso normal')
elif imc >= 25 and imc < 30:
  print('Sobrepeso')
else:
  print('Obesidade')

#4-Crie um programa que calcule o bônus de um funcionário com base no tempo de serviço:

tempo = int(input('Insira o tempo de serviço: '))
salario = float(input('Insira o Salario: '))

if tempo < 1:
  print('Sem bônus para menos de 1 ano. ' f'Salario: {salario:.2f}')
elif tempo >= 1 and tempo < 3:
  salario *= 1.05
  print('Bônus de 5% para 1 a 3 anos. ' f'Salario: {salario:.2f}')
elif tempo >= 3 and tempo < 5:
  salario *= 1.1
  print('Bônus de 10% para 3 a 5 anos. ' f'Salario: {salario:.2f}')
else:
  salario *= 1.15
  print('Bônus de 15% para mais de 5 anos. ' f'Salario: {salario:.2f}')

#5-Escreva um programa que leia a velocidade de um veículo e a classifique em:

velocidade = float(input('Insira a velocidade: '))

if velocidade <= 40:
  print('Baixa velocidade')
elif velocidade >= 41 and velocidade < 80:
  print('Velocidade Moderada')
elif velocidade >= 81 and velocidade < 120:
  print('Velocidade alta')
else:
  print('Velocidade muito alta')

#Desafio

#Generais => Acesso total
#Soldados => Apenas em missao ou acompanhados
#cientistas => Somente acima do nivel 5
#civis => Familiares diretos de militares de alta patente OU VISITAS DE SEGUNDA OU QUINTA

#Hackers eticos => apresentar codigo valido ou se forem acompanhados de militar superior

patente = input('Insira sua patente: ').upper().strip()
nivel = input('Insira seu nivel(1-5): ')

#GENERAL
if patente == 'GENERAL':
  print('Acesso total')

#CIENTISTAS
if patente == 'CIENTISTA' and nivel == '5':
  print('Acesso total')

acompanhante = input('Insira a patente do acompanhante: ').upper().strip()
nivel = input('Insira seu nivel(1-5): ')
if patente == 'CIENTISTA' and acompanhante == 'GENERAL' or patente == 'CIENTISTA' and nivel == '5':
    print('Acesso total')

familiar = input('Insira o Familiar: ').upper().strip()
dia = input('Insira o dia da semana: ').upper().strip()

#CIVIS
dia = ['SEGUNDA-FEIRA', 'TERCA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA']

if patente == 'CIVIL' and dia == 'SEGUNDA-FEIRA' or dia == 'QUINTA-FEIRA':
  print('Acesso Permitido')
  if patente == 'CIVIL' and familiar == 'GENERAL' or familiar == 'CIENTISTA':
    print('Acesso Permitido')

codigo = input('Insira o Codigo: ')
#HACKERS
if patente == 'HACKER' and codigo == '1232025':
  print('Acesso total')

  acompanhante = input('Insira a patente do acompanhante: ').upper().strip()
  nivel = input('Insira seu nivel(1-5): ')
  if patente == 'HACKER' and acompanhante == 'GENERAL' or patente == 'CIENTISTA' and nivel == '5':
    print('Acesso total')

#DEMAIS

else:
  print('Acesso Negado!')