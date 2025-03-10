try:

    texto = input('Insira o texto: ').lower().strip()
    caractere = input('Insira o caractere desejado: ').lower().strip()

    def contar_caracteres(texto, caractere):
        contador = 0
        for i in texto:
            if i == caractere:
                contador += 1
        return contador

    print(f'O numero de vezes que {caractere} aparece em {texto} e {contar_caracteres(texto, caractere)}')
except ValueError:
    print('O valor deve ser uma string!')
