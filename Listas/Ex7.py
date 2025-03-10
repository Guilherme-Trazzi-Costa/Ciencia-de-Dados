lista = ['abacaxi', 'amora', 'banana', 'uva', 'uva', 'amora']
contador = 0
palavra = input('Insira uma fruta: ').lower().strip()
for n in lista:
    if palavra == n:
        contador += 1
print(f'A fruta {palavra}, aparece {contador} vezes')
    