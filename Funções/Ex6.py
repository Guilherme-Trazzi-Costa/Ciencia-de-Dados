texto = input('Insira a palavra: ').lower()

def palindromo(texto):
  invertido = texto[::-1]
  if texto == invertido:
    return 'True'
  else:
    return 'False'
print(palindromo(texto))

