USE db_biblioteca;

SELECT * FROM tb_autores;

-- EXERCICIO 1. Crie uma stored procedure que insira um novo autor na tabela Autores.
DELIMITER $$

CREATE PROCEDURE InserirAutor(
IN p_id_autor INT,
IN p_nome VARCHAR(255),
IN p_data_nascimento DATE
)

BEGIN 
	INSERT INTO tb_autores(id_autor, nome, data_nascimento)
    VALUES(p_id_autor, p_nome, p_data_nascimento);
END $$

DELIMITER ;

DROP procedure InserirAutor;
CALL InserirAutor( '6', 'Jair', '1980-05-25', '46');


-- EXERCICIO 2. Crie uma stored procedure para atualizar a data de devolução de um empréstimo já registrado.
SELECT * FROM tb_emprestimos;

DELIMITER $$
CREATE PROCEDURE AtualizaDevo(
IN p_id_emprestimo INT,
IN p_data_devolucao DATE
)

BEGIN
	UPDATE tb_emprestimos SET data_devolucao = p_data_devolucao WHERE id_emprestimo = p_id_emprestimo;
END $$

DELIMITER ;

CALL AtualizaDevo('5', '2025-03-05');

-- EXERCICIO 3. Crie uma stored procedure que consulte todos os livros emprestadospor um determinado membro, retornando os títulos dos livros e as datas de empréstimo.
SELECT * FROM tb_membros;
SELECT * FROM tb_emprestimos;

DELIMITER $$
CREATE PROCEDURE VerLivros(
IN p_id_membro INT
)

BEGIN
	SELECT M.nome, L.titulo, E.data_emprestimo FROM tb_emprestimos AS E
    INNER JOIN tb_membros AS M
    ON E.id_membroE = M.id_membro
    INNER JOIN tb_livros AS L
    ON E.id_livroE = L.id_livro
    WHERE id_membro = p_id_membro;
END $$

DELIMITER ;
CALL VerLivros('3');