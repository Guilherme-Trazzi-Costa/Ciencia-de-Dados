#1-Verifique se um numero é positivo

Numero = -18

if Numero > 0:
  print('O Numero é maior que 0')

#2-Verificar se idade eh maior que 18

idade = 19

#if condicao

if idade >= 18:
  print('Voce e maior de idade')
else:
  print('Menor de idade')

#3-Peça um número ao usuário e exiba &quot;Número par&quot; se ele for divisível por 2.
n1 = int(input('Insira um numero '))
if (n1 % 2) == 0:
  print('O numero é par')
else:
  print('O numero é impar')

#4-Se a temperatura informada pelo usuário for maior que 30°C, exiba Está quente!
temp = float(input("Insira uma temperatura: "))
if temp > 30:
  print("Está Quente")
else:
  print('Esta Frio!')

#5-Se a nota de um aluno for maior ou igual a 6, exiba &quot;Aprovado
nota = 4
if nota >= 6:
  print("Aprovado")
else:
  print('Reprovado')

#6-Se a senha digitada pelo usuário for &quot;1234&quot;, exiba &quot;Acesso permitido&quot;.
senha = str(input("Insira a senha: "))
if senha == "1234":
  print("Acesso Permitido")
else:
  print('Acesso Negado')

#7- Se o valor da compra for maior que R$100,00, exiba &quot;Você ganhou um desconto!&quot;.
compra = round(float(input("Valor total de: ")),2)
if compra > 100.00:
  print("Voce Ganhou um desconto!")
else:
  print('Sem desconto')

#8-Peça um número ao usuário e exiba &quot;Número maior que 100&quot; se ele for maior que 100.

numero = int(input('Insira um numero: '))
if numero > 100:
  print('Número maior que 100')
else:
  print('Numero menor que 100')

#9-Se a velocidade informada for maior que 80 km/h, exiba &quot;Você foi multado.
velocidade = float(input('Insira a Velocidade:'))
if velocidade > 80:
  print('Voce foi multado')

#10-Se o ano informado for divisível por 4, exiba &quot;Ano bissexto&quot;.
ano = int(input('Insira o ano: '))
if ano % 4 == 0:
  print('Ano Bissexto')
else:
  print('Ano nao Bissexto')

dia = input('Insira o dia da semana: ').upper().strip()
if dia != 'SABADO' and dia != 'DOMINGO':
  print('Dia da Semana')
else:
  print('Fim de Semana')