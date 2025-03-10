#Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.
total = 0
for i in range(5):
    cliente = input(f'Insira o {i} Cliente: ')
    faturamento = float(input('Insira o faturamento: '))

    total += faturamento

if total >= 54000:
    print(f'O faturamento superou a meta da loja B em {total - 54000:.2f}')
else:
    print(f'O faturamento nao superou a loja B {54000 - total:.2f}')

