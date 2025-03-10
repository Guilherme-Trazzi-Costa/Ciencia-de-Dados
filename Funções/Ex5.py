numero = int(input("Entre com um numero: "))

def tabuada(numero):
    for i in range(1, 11):
       resultado = print(f'{i} X {numero} = {i*numero}')
    return resultado
print(tabuada(numero))