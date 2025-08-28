USE db_biblioteca;


--  Exercicio 1. Crie uma função que recebe o id_autor e retorna a idade do autor com base na data de nascimento.
 DELIMITER $$
 
 CREATE FUNCTION idade_autor(p_id_autor INT)
 RETURNS INT 
 READS SQL DATA
 BEGIN
	DECLARE idadea INT;
	SELECT timestampdiff(YEAR, data_nascimento, curdate()) INTO idadea FROM tb_autores WHERE id_autor = p_id_autor;
    RETURN idadea;
END $$

DELIMITER ;

SELECT idade_autor('2');

-- Exercicio 2. Crie uma função que recebe o id_autor e retorna a quantidade de livros escritos por esse autor.

DELIMITER $$

CREATE FUNCTION qtd_livros(p_id_autor INT)
RETURNS INT 
READS SQL DATA
BEGIN
	DECLARE nlivros INT;
    SELECT COUNT(id_livro) INTO nlivros FROM tb_livros WHERE id_autorL = p_id_autor;
    RETURN nlivros;
END $$

DELIMITER ;

SELECT qtd_livros('2');


-- Exercicio 3. Crie uma função que recebe duas datas e retorna o total de empréstimos realizados nesse período.
SELECT * FROM tb_emprestimos;

DELIMITER $$
CREATE FUNCTION per_emprestimo(p_data_inic DATE, p_data_fim DATE)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE qtd_livro INT;
    SELECT COUNT(id_livroE) INTO qtd_livro FROM tb_emprestimos WHERE p_data_inic <= data_emprestimo AND data_emprestimo <= p_data_fim;
    RETURN qtd_livro;
END $$

DELIMITER ;
DROP FUNCTION per_emprestimo;
SELECT per_emprestimo('2025-03-01', '2025-05-20');
-- (P_data_inic <= data_emprestimo <= p_data_fim)
-- Exercicio 4. Crie uma função que retorna a média de dias em que os livros foram emprestados.

SELECT * FROM tb_emprestimos;
DELIMITER $$

CREATE FUNCTION med_livros(p_id_livro INT)
RETURNS INT
READS SQL DATA
BEGIN
	DECLARE mlivros INT;
    SELECT AVG(timestampdiff(day, data_emprestimo, data_devolucao)) INTO mlivros FROM tb_emprestimos WHERE id_livroE = p_id_livro;
    RETURN mlivros;
END $$

DELIMITER ;
DROP FUNCTION med_livros;
SELECT med_livros('1');