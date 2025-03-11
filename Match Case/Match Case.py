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
    print('Numero invalido')

#Exercício 1

#Peça ao usuário para digitar três lados de um triângulo e use match case para classificar o triângulo como:

#• Equilátero (todos os lados iguais)
#• Isósceles (dois lados iguais)
#• Escaleno (todos os lados diferentes)

Lado1 = float(input('Insira o primeiro lado: '))
Lado2 = float(input('Insira o segundo lado: '))
Lado3 = float(input('Insira o terceiro lado: '))


match (Lado1, Lado2, Lado3):
  case (Lado1, Lado2, Lado3) if Lado1 == Lado2 == Lado3:
    print('Equilatero')
  case (Lado1, Lado2, Lado3) if Lado1 != Lado2 != Lado3 != Lado1:
    print('Escaleno')
  case (Lado1, Lado2, Lado3) if Lado1 == Lado3 or Lado1 == Lado2 or Lado2 == Lado3:
    print('Isosceles')

#Exercicio 2

#Peça ao usuário dois números e um operador matemático (+, -, *, /) e
#use match-case para calcular e exibir o resultado. Caso o operador
#seja inválido, exiba uma mensagem de erro.

n1 = float(input('Insira um numero: '))
n2 = float(input('Insira um numero: '))

operador = input('Insira um operador Matematico(+, -, *, /): ')

match operador:
  case '+':
    print(f'A soma dos numeros e: {n1 + n2}')
  case '-':
    print(f'A soma dos numeros e: {n1 - n2}')
  case '*':
    print(f'A soma dos numeros e: {n1 * n2}')
  case '/':
    print(f'A soma dos numeros e: {n1 / n2}')
  case '^':
    print(f'A soma dos numeros e: {n1 ** n2}')
  case _:
    print('Operador nao identificado')
