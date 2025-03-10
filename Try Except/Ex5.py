try:
    numeros = list(map(int, input('Insira uma lista de numeros separados por espaco: ').split()))

    def soma_lista(numeros):
        return sum(numeros)

    print(f'A soma da lista e: {soma_lista(numeros)}')

except TypeError:
    print('A lista nao pode estar vazia, insira um numero')
except ValueError:
    print('Valor invalido!')