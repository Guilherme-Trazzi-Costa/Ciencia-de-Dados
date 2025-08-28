USE db_carro;

-- Proprietários de carros acima da média de preço
-- Liste o nome dos proprietários que possuem carros com valor acima da média
-- de todos os carros.

SELECT * FROM tb_proprietario;

SELECT AVG(valor) FROM tb_carro;

SELECT P.nome, C.valor FROM tb_proprietario AS P
LEFT JOIN tb_carro AS C
ON P.id_carroF = C.id_carro
WHERE valor > (SELECT AVG(valor) FROM tb_carro);


-- Carros vendidos mais que a média geral de vendas
-- Liste os modelos de carro cujo numero_vendas seja maior que a média de
-- vendas de todos os carros.

 SELECT * FROM tb_carro;
 
 SELECT AVG(numero_vendas) FROM tb_carro;
 
 SELECT modelo, marca, numero_vendas FROM tb_carro
 WHERE numero_vendas > (SELECT AVG(numero_vendas) FROM tb_carro);
 
 
-- Carros que já tiveram valor acima da média histórica
-- Mostre os carros cujo valor já foi maior que a média de todos os valores
-- registrados no histórico.]

SELECT * FROM tb_carro;
SELECT * FROM tb_historico;

SELECT AVG(valor_anterior) FROM tb_historico;

SELECT modelo, marca, valor FROM tb_carro AS C
LEFT JOIN tb_historico AS H
ON C.id_carro = H.id_carroH
WHERE valor_novo > (SELECT AVG(valor_anterior) FROM tb_historico);


-- Carros sem histórico de alteração de preço
-- Liste os modelos de carros que não aparecem na tabela historico_preco.
SELECT * FROM tb_carro;
SELECT * FROM tb_historico;

SELECT * FROM tb_carro
WHERE id_carro NOT IN (SELECT id_carroH FROM tb_historico);




