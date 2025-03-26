Faturamento = 1200 #int

Custo = 750.55 #float

Novas_Vendas = 100

Faturamento = Faturamento + Novas_Vendas

Imposto = Faturamento * 0.1

Lucro = Faturamento - Custo - Imposto

Margem = Lucro / Faturamento



print("Faturamento foi de ", Faturamento)
print("O custo foi de ", Custo) 
print("O lucro foi de ", Lucro) 
print("A margem de lucro foi ", round(Margem, 2))

mensagem = "O Faturamento da loja foi", Faturamento #string

teve_lucro = True #Boolean

Tempo_Contrato = 170
Tempo_Anos = Tempo_Contrato/12
print("Tempo em anos", Tempo_Anos)
Tempo_Meses = 170 %12
print("Tempo em Meses", Tempo_Meses)
