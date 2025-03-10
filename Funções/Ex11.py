texto = input('Insira a palavra: ').lower()
anagrama = input('Insira o anagrama: ')
def palindromo(texto):
  invertido = texto[::-1]
  if invertido == anagrama:
    return 'True'
  else:
    return 'False'
print(palindromo(texto))