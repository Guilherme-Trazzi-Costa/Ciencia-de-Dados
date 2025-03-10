try:
    numeros = list(map(int, input('Insira uma lista de numeros separados por espaco: ').split()))
    indice = int(input('Insira o numero do indice: '))
    def pegar_elementos(numeros, indice):
        
        return numeros[indice]
    print(pegar_elementos(numeros, indice))

except TypeError:
    print('A lista nao pode estar vazia, insira um numero')
except ValueError:
    print('Valor invalido!')
except IndexError:
    print('O indice nao corresponde a um item na lista')