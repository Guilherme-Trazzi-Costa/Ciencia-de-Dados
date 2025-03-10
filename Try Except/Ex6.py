try:
    a = int(input('Insira o dividendo: '))

    b = int(input('Insira o divisor: '))

    def multiplicar(a,b):

            return a * b

    print(multiplicar(a, b))
except TypeError:
    print('A lista nao pode estar vazia, insira um numero')
except ValueError:
    print('Valor invalido!')