-- Subqueries carro
USE db_carro;
-- 1. Quais carros tem preço acima da média
-- Primeiro: Calcular coluna
SELECT AVG(valor) FROM tb_carro;

-- Criar a consulta a partir do cálculo acima
SELECT * FROM tb_carro WHERE valor > (SELECT AVG(VALOR) FROM tb_carro);