USE clinicavetbd;

-- Exercicio 1. Crie uma função que receba o id_cliente e retorne a quantidade de pets que esse cliente possui.
DELIMITER $$

CREATE FUNCTION QtdPet(p_id_clienteP INT(3))
RETURNS INT(3)
READS SQL DATA
BEGIN
	DECLARE quantidade INT(3);
	SELECT COUNT(id_pet) INTO quantidade FROM tb_pets WHERE id_clienteP = p_id_clienteP;  
    RETURN quantidade;
END $$

DELIMITER ;
drop function QtdPet;
SELECT QtdPet('3');

-- Exercicio 2. Crie uma função que recebe o id_pet e retorna a data da última consulta do pet.
 
DELIMITER $$
CREATE FUNCTION data_consulta(p_id_pet INT)
RETURNS DATE
READS SQL DATA
BEGIN
	DECLARE consulta DATE;
    SELECT MAX(data_atendimento) INTO consulta FROM tb_atendimentos WHERE id_petA = p_id_pet;
    RETURN consulta;
END $$

DELIMITER ;

DROP FUNCTION DATA_CONSULTA;
SELECT data_consulta('1');

-- Exercicio 3. Crie uma função que receba o id_veterinario e retorne o número total de atendimentos feitos por ele.
DELIMITER $$

CREATE FUNCTION Natendimentos(p_id_veterinario INT)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE atendimento INT;
	SELECT COUNT(id_atendimento) INTO atendimento FROM tb_atendimentos WHERE id_veterinarioA = p_id_veterinario;
    RETURN atendimento;
END $$

DELIMITER ;

SELECT Natendimentos('3');


