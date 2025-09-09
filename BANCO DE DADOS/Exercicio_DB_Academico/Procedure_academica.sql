USE db_academico;

-- Exercício 1: Crie uma procedure chamada insere_professor que insere um professor na tabela professores e retorna o ID gerado.
DELIMITER $$

CREATE PROCEDURE insere_professor(
IN p_id_professor INT,
IN p_nome VARCHAR(100),
IN p_departamento VARCHAR(100),
IN p_ano_admissao INT
)

BEGIN 
	INSERT INTO tb_professores(id_professor, nome, departamento, ano_admissao)
    VALUES(p_id_professor, p_nome, p_departamento, p_ano_admissao);
END $$

DELIMITER ;

DROP PROCEDURE insere_professor;
SELECT * FROM tb_professores;
CALL insere_professor('6', 'Tulio Zacarias', 'Advocacia e Direito', '2012');

-- Exercício 2: Crie uma procedure chamada atualiza_disciplina que recebe o ID de uma disciplina e atualiza o nome dessa disciplina.

DELIMITER $$
CREATE PROCEDURE atualiza_disciplina(
IN p_id_disciplina INT,
IN p_nome VARCHAR(100)
)
BEGIN
	UPDATE tb_disciplinas SET nome = p_nome WHERE id_disciplina = p_id_disciplina;
END $$

DELIMITER $$

CALL atualiza_disciplina('4', 'Anatomia');

-- Exercício 3: Crie uma procedure chamada remove_estudante que remove um estudante da tabela estudantes com base no ID passado como parâmetro.
DELIMITER $$
CREATE PROCEDURE remove_estudante(
IN p_id_estudante INT
)

BEGIN
	DELETE FROM tb_matriculas tb_estudantes WHERE p_id_estudante = id_estudante;
END $$

DELIMITER ;

DROP PROCEDURE remove_estudante;
CALL remove_estudante('5');

-- Exercício 4: Crie uma procedure chamada consulta_professor que retorna o nome e departamento de um professor com base no ID passado.
DELIMITER $$
CREATE PROCEDURE consulta_professor(
IN p_id_professor INT
)

BEGIN
	SELECT nome, departamento FROM tb_professores WHERE id_professor = p_id_professor;
END $$

DELIMITER ;

CALL consulta_professor('1');

-- Exercício 5: Crie uma procedure chamada atualiza_nota que atualiza a nota de um estudante para uma disciplina específica, com base no ID da matrícula.

DELIMITER $$ 
CREATE PROCEDURE atualiza_nota(
IN p_id_matricula INT,
IN p_nota DECIMAL(10,2)
)

BEGIN
	SELECT M.id_matricula, E.nome, N.nota FROM tb_notas AS N
    INNER JOIN tb_matriculas AS M
    ON N.id_matricula = M.id_matricula
    INNER JOIN tb_estudantes AS E
    ON E.id_estudante = M.id_estudante
    WHERE M.id_matricula = p_id_matricula;
    
	UPDATE tb_notas SET nota = p_nota
    WHERE id_matricula = p_id_matricula;
END $$

DELIMITER ;

CALL atualiza_nota('5', '7.0');



