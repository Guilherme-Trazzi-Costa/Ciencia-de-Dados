USE db_biblioteca;

-- a. Liste os autores que possuem livros com ano de publicação maior que a média de anos de publicação de todos os livros cadastrados.

SELECT A.nome, L.titulo, L.ano_publicacao FROM tb_livros AS L
INNER JOIN tb_autores AS A
ON L.id_autorL = A.id_autor
WHERE ano_publicacao > (SELECT AVG(ano_publicacao) FROM tb_livros);

-- b. Liste os livros que foram emprestados ao menos uma vez.
SELECT L.titulo, E.id_livroE FROM tb_emprestimos AS E
INNER JOIN tb_livros AS L
ON L.id_livro = E.id_livroE
WHERE id_livroE IN (SELECT id_livroE FROM tb_emprestimos);

-- c. Consulte os livros que ainda não foram emprestados.
SELECT L.titulo, E.id_livroE FROM tb_emprestimos AS E
INNER JOIN tb_livros AS L
ON L.id_livro = E.id_livroE
WHERE id_livroE NOT IN (SELECT id_livroE FROM tb_emprestimos);