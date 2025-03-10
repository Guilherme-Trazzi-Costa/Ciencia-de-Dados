# Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.

compra = int(input('Insira o valor da compra: '))
for i in range(500, 3100, 100):
    desconto = min((i - 500) //100 + 1, 25)
    valor_final = i -(i*(desconto/100))
    print(f'Valor da compra: {compra} || Porcentagem: {desconto} || Valor final: {valor_final}')

