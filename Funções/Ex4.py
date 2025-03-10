num = int(input('Insira um numero: '))

def fatorial(num):
    resultado = 1
    for i in range(2, num + 1):
        resultado*= i
    return resultado

print(fatorial(num))