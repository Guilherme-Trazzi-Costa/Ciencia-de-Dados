USE db_carro;
-- Função - Realiza consultas e caso precise, realizar calculos
-- Calculo de descontos

DELIMITER $$
CREATE FUNCTION CalcularDesconto(valor DECIMAL(10,2), desconto DECIMAL(5,2))
RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
	RETURN valor - (valor * desconto/100);
END $$

DELIMITER ;

SELECT marca, modelo, valor, CalcularDesconto(valor, 20) AS 'Valor com Desconto' FROM tb_carro;


-- Vendas por marca

DELIMITER $$
CREATE FUNCTION Valor_Marca(p_marca VARCHAR(255))
RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
	DECLARE valor_total DECIMAL(50,2);
	SELECT SUM(valor*numero_vendas) INTO valor_total FROM tb_carro WHERE marca = p_marca;
    RETURN valor_total;
END $$

DELIMITER ;

SELECT Valor_Marca('Fiat');

