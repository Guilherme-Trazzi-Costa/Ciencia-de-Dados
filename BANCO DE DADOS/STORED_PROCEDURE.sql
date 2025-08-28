USE db_carro;

-- STORED PROCEDURE
-- Quando precisa armazenar um bloco de código que pode envolver multiplas operações(INSERT, UPDATE, DELETE)

-- CRIAR PROCEDURE QUE INSIRA UM NOVO CARRO NA TABELA
DELIMITER $$
CREATE PROCEDURE InserirCarro(
IN p_id_carro INT,
IN p_marca VARCHAR(255),
IN p_modelo VARCHAR(255),
IN p_ano INT,
IN p_valor DECIMAL(10,2),
IN p_cor VARCHAR(255),
IN p_numero_vendas INT
)

BEGIN
	INSERT INTO tb_carro (id_carro, marca, modelo, ano, valor, cor, numero_vendas) 
    VALUES (p_id_carro, p_marca, p_modelo, p_ano, p_valor, p_cor, p_numero_vendas);
END $$

DELIMITER ;
drop procedure InserirCarro;
CALL InserirCarro ('8', 'Fiat', 'FastBack', '2005', '13000', 'Strato', '52000');

SELECT * FROM tb_carro;