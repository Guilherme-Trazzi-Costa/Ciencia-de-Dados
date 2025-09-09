USE db_academico;

-- Exercício 1: Crie uma função chamada idade_estudante que receba a data de nascimento de um estudante e retorne à idade.

DELIMITER $$

CREATE FUNCTION idade_estudante(p_id_estudante DATE)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE idade INT;
    SELECT timestampdiff(YEAR, data_nascimento, CURDATE()) INTO idade FROM tb_estudantes WHERE p_id_estudante = id_estudante;
    RETURN idade;
END $$

DELIMITER ;


DROP FUNCTION idade_estudante;
SELECT idade_estudante('2003-10-15');

-- Exercício 2: Crie uma função chamada total_estudantes_disciplina que receba o ID de uma disciplina e retorne o número de estudantes matriculados nela.

DELIMITER $$
CREATE FUNCTION total_estudantes_disciplina(p_id_disciplina INT)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE total_estudantes INT;
    SELECT COUNT(id_estudante) AS 'Total Estudantes' INTO total_estudantes FROM tb_estudantes AS E
    INNER JOIN tb_cursos AS C
    ON E.id_curso = C.id_curso
    INNER JOIN tb_disciplinas AS D
    ON D.id_curso = C.id_curso
    WHERE p_id_disciplina = id_disciplina;
	RETURN total_estudantes;
END $$

DELIMITER ;

SELECT total_estudantes_disciplina('1');


-- Exercício 3: Crie uma função chamada nota_maxima que retorne a maior nota registrada na tabela notas.

DELIMITER $$
CREATE FUNCTION nota_maxima()
RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN 
	DECLARE max_nota DECIMAL(10,2);
    SELECT MAX(nota) INTO max_nota FROM tb_notas ORDER BY nota DESC LIMIT 1;
	RETURN max_nota;
END $$

DELIMITER ;

DROP FUNCTION nota_maxima;
SELECT nota_maxima() AS 'MAIOR NOTA' FROM tb_notas;

-- Exercício 4: Crie uma função chamada disciplina_do_curso que receba o ID de um urso e retorne o nome da disciplina associada.

DELIMITER $$
CREATE FUNCTION disciplina_do_curso(p_id_curso INT)
RETURNS VARCHAR(100)
READS SQL DATA
BEGIN
	DECLARE disciplina_curso VARCHAR(100);
    SELECT D.nome INTO  disciplina_curso  FROM tb_disciplinas AS D
    INNER JOIN tb_cursos AS C
    ON D.id_curso = C.id_curso
    WHERE p_id_curso = D.id_curso;
    RETURN disciplina_curso;
END $$

DELIMITER ;
DROP FUNCTION disciplina_do_curso;
SELECT disciplina_do_curso('1');
    
    
-- Exercício 5: Crie uma função chamada media_notas_curso que receba o ID de um curso e retorne a média das notas dos estudantes matriculados nesse curso.
DELIMITER $$

CREATE FUNCTION media_notas_curso(p_id_curso INT)
RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
	DECLARE media_curso DECIMAL(10,2); 
    SELECT AVG(nota) INTO media_curso FROM tb_notas AS N
    INNER JOIN tb_matriculas AS M
    ON N.id_matricula = M.id_matricula
    INNER JOIN tb_estudantes AS E
    ON M.id_estudante = E.id_estudante
    INNER JOIN tb_cursos AS C
    ON C.id_curso = E.id_curso
    WHERE p_id_curso = C.id_curso;
    RETURN media_curso;
END $$

DELIMITER ;

DROP FUNCTION media_notas_curso;
SELECT media_notas_curso('3');