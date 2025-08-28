USE clinicavetbd;

-- EXERCICIO 1. Crie uma stored procedure que adicione um novo veterinário na tabela Veterinarios.
SELECT * FROM tb_veterinarios;

DELIMITER $$
CREATE PROCEDURE InserirVeterinario(
IN p_id_veterinario INT,
IN p_nome VARCHAR(255),
IN p_especialidade VARCHAR(255),
IN p_telefone VARCHAR(255)
)

BEGIN
	INSERT INTO tb_veterinarios (id_veterinario, nome, especialidade, telefone)
    VALUES(p_id_veterinario, p_nome, p_especialidade, p_telefone);
END $$

DELIMITER ;
CALL InserirVeterinario ('5','Josealdo', 'Clinico Geral', '8765-4321');


-- EXERCICIO 2. Crie uma stored procedure para atualizar os dados de um cliente, como nome, endereço e telefone.

SELECT * FROM tb_clientes;

DELIMITER $$

CREATE PROCEDURE AtualizaCliente(
IN p_id_cliente INT,
IN p_endereco VARCHAR(255),
IN p_telefone VARCHAR(255)
)

BEGIN
	UPDATE tb_clientes SET endereco = p_endereco, telefone = p_telefone WHERE id_cliente = p_id_cliente;
END $$

DELIMITER ;

CALL AtualizaCliente('2', 'São Bernardo', '1234-5698');

-- EXERCICIO 3. Crie uma stored procedure que registre um novo atendimento de um pet, verificando se o veterinário e o pet existem.


SELECT * FROM tb_pets;
SELECT * FROM tb_atendimentos;
SELECT * FROM tb_veterinarios;

DELIMITER $$
CREATE PROCEDURE InserirAtend(
IN p_id_atendimento INT,
IN p_id_petA INT,
IN p_id_veterinarioA INT,
IN p_data_atendimento DATE,
IN p_descricao VARCHAR(255)
)

BEGIN
	  IF NOT EXISTS (SELECT * FROM tb_pets WHERE id_petA = p_id_petA AND id_veterinarioA = p_id_veterinarioA) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Pet não encontrado';
    END IF;


	INSERT INTO tb_atendimentos(id_atendimento, id_petA, id_veterinarioA, data_atendimento, descricao)
    VALUES(p_id_atendimento, p_id_petA, p_id_veterinarioA, p_data_atendimento, p_descricao);

END $$

DELIMITER ;

DROP PROCEDURE InserirAtend;
CALL InserirAtend('5','2', '2','2025-08-25', 'Alguma coisa');

    