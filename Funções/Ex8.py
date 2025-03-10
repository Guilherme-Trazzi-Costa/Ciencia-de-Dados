lista = [2, 4, 9, 7, 5, 3, 6]

def media_notas(lista):
    return sum(lista)/len(lista)

print(f'{media_notas(lista):.2f}')