palavra = input('Digite uma palavra: ').lower()

vogais = 'aeiou'

def qtd_vogais(palavra):
    quantidadevogais = 0
    for letra in palavra:
        if letra in vogais:
            quantidadevogais += 1
    return quantidadevogais
print(f'A palavra {palavra} tem {qtd_vogais(palavra)} vogais')