-- Exemplo 5 Mostrar produtos maiores que 1800 R$
Select * 
From produtos
Where Preco_Unit > 1800;


-- Exemplo 5 Mostrar produtos iguais a 3100 R$
Select * 
From produtos
Where Preco_Unit = 3100;

-- Exemplo 5 Mostrar produtos iguais a Dell
Select * 
From produtos
Where Marca_Produto = 'Dell';

-- Exemplo 5 Mostrar pedidos feitos 03/01/2019
Select * 
From pedidos
Where Data_Venda = '2019-01-03';


-- Exemplo 5 Mostrar clientes solteiros e masculinos
Select * 
From clientes
Where Estado_Civil = 'S' And Sexo = 'M';

-- Exemplo 5 Mostrar clientes solteiros e masculinos
Select * 
From produtos
Where Marca_Produto = 'Dell' Or Marca_Produto = 'Samsung';
