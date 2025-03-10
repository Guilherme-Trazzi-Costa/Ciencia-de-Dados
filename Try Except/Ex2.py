

def ler_inteiro():

    while True:
        try:
            num = int(input('Insira um numero inteiro valido: '))

            return print(f' O numero {num} e valido !')
        except ValueError:
            print('Numero invalido!')
numero = ler_inteiro()





