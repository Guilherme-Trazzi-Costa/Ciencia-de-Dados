#1. Leia dois números, faça a soma e apresente caso seja maior que 15.

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira o segundo numero: '))

soma = n1 + n2

if soma > 15:
  print('Soma maior do que 15:', soma)

#2. Faça um programa que recebendo um valor inteiro, informe se o número épositivo, negativo ou neutro.

n1 = int(input('Insira um numero: '))

if n1 > 0:
  print('O numero e positivo')
elif n1 == 0:
  print('O numero e neutro')
else:
  print('O numero e negativo')

#3. Leia a idade e informe se a pessoa é maior ou menor de idade

idade = int(input('Insira a idade: '))

if idade > 18:
  print('Maior de idade')
else:
  print('Menor de idade')

#4. Faça um programa que pergunte a temperatura atual para o usuário e mostreuma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.

temperatura = int(input('Insira a temperatura: '))

if temperatura < 15:
  print('muito frio')
elif temperatura <= 20:
  print('frio')
elif  temperatura <= 26:
  print('Agradavel')
else:
  print('quente')

#5. Faça um programa em linguagem Python que leia dois números inteiros e informe se estes são iguais ou diferentes.

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira o segundo numero: '))

if n1 == n2:
  print('Os numeros sao iguais')
else:
  print('Os numeros sao diferentes')

#6. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234.

senha = input('Insira a senha: ')

if senha == '1234':
  print('ACESSO PERMITIDO')
else:
  print('ACESSO NEGADO')

#7-Ler duas notas de um aluno, efetuar a média aritmética e, se a média for maior ou igual a 7, informar que o aluno foi aprovado;
n1 = float(input('Entre com uma nota: '))
n2 = float(input('Entre com a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
  print('Aluno aprovado !', 'Media: ', media)
elif media >= 5 and media < 7:
  print('O aluno esta de exame !', 'Media: ', media)
else:
  print('Aluno reprovado !', 'Media:', media)

#8. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol

g1 = int(input('Insira os gols do primeiro time: '))
g2 = int(input('Insira os gols do segundo time: '))

if g1 > g2:
  print('O primeiro time ganhou!')
elif g1 == g2:
  print('Os times empataram!')
else:
  print('O segundo time ganhou!')

#9. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M matutino, V Vespertino ou N Noturno.

turno = input('Insira seu turno:(M/V/N)').upper().strip()

match turno:
  case 'M':
    print('Bom Dia!')
  case 'V':
    print('Boa Tarde!')
  case 'N':
    print('Boa Noite!')
  case _:
    print('Turno indefinido!')

#10. Faça um programa que solicite ao usuário sua idade

idade = int(input('Insira a idade: '))

match idade:
  case idade  if 0 <= idade <= 11:
    print('Crianca')
  case idade if 12 <= idade <= 18:
    print('Adolescente')
  case idade if 19 <= idade <= 24:
    print('Jovem')
  case idade if 25 <= idade <= 40:
    print('Adulto')
  case idade if 41 <= idade <= 60:
    print('Meia Idade')
  case idade if idade > 60:
    print('Idoso')
  case _:
    print('Idade invalida!')

#11. Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

salario = float(input('Insira seu salario: '))

match salario:
  case salario if salario <= 280.00:
    reajuste = salario*1.2
    print('Salario antigo: ', salario)
    print('Percentual de aumento: 20%')
    print(f'Valor do aumento: {salario*0.2}')
    print('Salario reajustado: ', reajuste)
  case salario if 280.00 <=salario <= 700.00:
    reajuste = salario*1.15
    print('Salario antigo: ', salario)
    print('Percentual de aumento: 15%')
    print(f'Valor do aumento: {salario*0.15}')
    print('Salario reajustado: ', reajuste)
  case salario if 700.00 <=salario <= 1500.00:
    reajuste = salario*1.1
    print('Salario antigo: ', salario)
    print('Percentual de aumento: 10%')
    print(f'Valor do aumento: {salario*0.1}')
    print(f'Salario reajustado: {reajuste:.2f}')
  case salario if salario> 1500.00:
    reajuste = salario*1.05
    print('Salario antigo: ', salario)
    print('Percentual de aumento: 5%')
    print(f'Valor do aumento: {salario*0.05}')
    print('Salario reajustado: ', reajuste)
  case _:
    print('Valor Invalido')

#12. Faça um Programa que leia um número e exiba o dia correspondente da semana.

dia = input('Insira um numero para o dia da semana(1-7): ')

match dia:
   case '1':
      print('Domingo')
   case '2':
      print('Segunda')
   case '3':
      print('Terca')
   case '4':
      print('Quarta')
   case '5':
      print('Quinta')
   case '6':
      print('Sexta')
   case '7':
      print('Sabado')
   case _:
    print('Invalido')

#13. Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit

conversao = input('Como deseja converter ?(F/C ou C/F) ').lower() #Fahreiheit para Celsius ou Celsius para Fahreiheit
temperatura = float(input('Insira o valor da temperatura: '))

match (conversao):
  case 'f/c':
    Celsius = (0.55*temperatura) -32
    print(f'A temperatura em graus Celsius e: {Celsius:.2f}')
  case 'c/f':
    Fahreinheit = (temperatura*1.8) + 32
    print(f'A temperatura em graus Fahreinheit e: {Fahreinheit:.2f}')
  case _:
    print('Selecao Invalida')

#14. Faça um programa que receba a idade de uma pessoa e imprima sua condição

idade = int(input('Insira a idade: '))

match idade:
  case idade if idade < 16:
    print('Proibido de votar')
  case idade if 16 <= idade < 18:
    print('Não são obrigadas a votar')
  case idade if 18 <= idade < 65:
    print('São obrigadas a votar')
  case idade if idade >= 65:
    print('Não são obrigadas a votar')
  case _:
    print('Idade invalida')

#15 e 16. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

telefone = input('Telefonou para a vítima?(sim/nao) ').lower()
local = input('Esteve no local do crime?(sim/nao) ').lower()
moradia = input('Mora perto da vítima?(sim/nao) ').lower()
divida = input('Devia para a vítima?(sim/nao) ').lower()
trabalho = input('Já trabalhou com a vítima?(sim/nao) ').lower()

lista =[telefone, local, moradia, divida, trabalho]
respostas = lista.count('sim')
match respostas:
  case respostas if respostas < 2:
    print('Nao participou do crime')
  case respostas if respostas == 2:
    print('Suspeita')
  case respostas if 2 < respostas <= 4:
    print('Cumplice')
  case resposta if resposta == 5:
    print('Assasino')
  case _:
    print('Resposta Invalida')

#17. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Insira o preco do produto 1: '))
produto2 = float(input('Insira o preco do produto 2: '))
produto3 = float(input('Insira o preco do produto 3: '))

if produto1 < produto2 < produto3 or produto1 < produto3 < produto2:
  print('O mais barato e o produto 1')
elif produto2 < produto1 < produto3 or produto2 < produto3 < produto1:
  print('O mais barato e o produto 2')
elif produto3 < produto1 < produto2 or produto3 < produto2 < produto1 :
  print('O mais barato e o produto 3')
else:
  print('Insira um valor valido')