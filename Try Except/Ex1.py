try:

    n1 = int(input('Insira o primeiro numero: '))
    n2 = int(input('Insira o segundo numero: '))

    op = input('Insira a operacao(+, -, *, /): ')

    resultado = 0
    def calculadora(n1, n2, op):

        match op:

            case '+':
                resultado = n1 + n2

            case '-':
                resultado = n1 - n2
            
            case '*':
                resultado =  n1 * n2
            
            case '/':
                resultado =  n1 / n2

        return resultado

    print(calculadora(n1, n2, op))

except ZeroDivisionError:
    print('Nao e permitido divisao por 0!')

except ValueError:
    print('Valor invalido!')


