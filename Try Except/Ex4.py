
try:
    a = int(input('Insira o dividendo: '))

    b = int(input('Insira o divisor: '))

    def divisao_segura(a,b):

            return a / b

    print(divisao_segura(a, b))
except ZeroDivisionError:
        print('Nao e possivel dividir por zero!')