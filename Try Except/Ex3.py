try:
    numeros = list(map(int, input('Insira uma lista de numeros separados por espaco: ').split()))

    def calcular_media(numeros):
        return sum(numeros)/len(numeros)

    print(f'A media da lista e: {calcular_media(numeros)}')

except TypeError:
    print('A lista nao pode estar vazia, insira um numero')
except ZeroDivisionError:
    print('Nao ha valor na lista para calcular a media!')