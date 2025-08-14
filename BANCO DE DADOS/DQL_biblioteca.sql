USE db_biblioteca;

SELECT * FROM tb_livros;
-- a) Livro com data de publicação mais antiga
SELECT titulo, ano_publicacao FROM tb_livros ORDER BY ano_publicacao ASC LIMIT 1;

-- b) Livro com data de publicacao mais recente
SELECT titulo, ano_publicacao FROM tb_livros ORDER BY ano_publicacao DESC LIMIT 1;

-- c) A quantidade de livros cadastrados no banco de dados
SELECT COUNT(id_livro) FROM tb_livros;

SELECT * FROM tb_emprestimos;
-- d) Consulte apenas os livros que possuam a data de devolução em 18-07-2024
SELECT id_livroE  AS 'Código do Livro' FROM tb_emprestimos WHERE data_devolucao = '2025-03-29';

-- e) Ordene o nome dos autores em ordem crescente
SELECT nome FROM tb_autores ORDER BY nome ASC;

-- f) Ordene o nome dos Livros em ordem decrescente
SELECT titulo FROM tb_livros ORDER BY titulo ASC;