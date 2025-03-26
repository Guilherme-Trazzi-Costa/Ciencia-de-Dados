lista = [1000, 500, 800, 1500, 2000, 2300]

meta = 1200
percentual_bonus = 0.1

for venda in lista:

    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0

    print(bonus)
