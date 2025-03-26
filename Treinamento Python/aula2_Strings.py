email = "meuemail@gmail.com"
faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro/faturamento

print(f"Faturamento da empresa: {faturamento}, Custo da empresa: {custo}, Lucro: {lucro}")

email_cliente = "qualquercoisa@terra.com"

email_cliente = email_cliente.upper()
print(email_cliente)

email_cliente = email_cliente.lower()
print(email_cliente)

print(email_cliente.find("@")) #-1 quando não verifica 

print(len(email_cliente))

print(email_cliente[0])

print(email_cliente[0:10]) #pedaço do texto

novo_email = email_cliente.replace("gmail.com","hotmail.com")

print(novo_email)

nome = "guilherme trazzi"

print(nome.capitalize())

print(nome.title())

#pegar servidor email
posicao_arroba = email_cliente.find("@") +1
servidor = email_cliente[posicao_arroba:]

print(servidor)


#pegar nome 

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]

#pegar sobrenome 

posicao_espaco = nome.find(" ")+1
segundo_nome = nome[posicao_espaco:]

print(primeiro_nome)
print(segundo_nome)

margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: {faturamento}, Custo da empresa: {custo}, Lucro: {lucro}, Margem: {margem_lucro:%}")
