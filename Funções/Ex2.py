num = int(input('Insira um numero: '))

def par_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
print(f'O numero inserido e: {par_impar(num)}')