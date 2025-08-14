USE db_biblioteca;

-- INER JOIN
-- 1. Liste o título do livro e o nome do autor.
SELECT L.titulo AS 'Titulo do livro', A.nome AS 'Nome Autor' FROM tb_livros AS L
INNER JOIN tb_autores AS A
ON L.id_autorL = A.id_autor;

-- 2. Liste o título do livro, o nome do autor e o ano de publicação.
SELECT L.titulo AS 'Titulo do Livro', A.nome AS 'Nome do Autor', L.ano_publicacao AS 'Ano de Publicacao' FROM tb_livros AS L
INNER JOIN tb_autores AS A
ON L.id_autorL = A.id_autor;

-- 3. Liste o nome do membro, o título do livro e a data de empréstimo.
SELECT M.nome AS 'Nome do Membro', L.titulo AS 'Titulo do Livro', E.data_emprestimo AS 'Data Emprestimo' FROM tb_emprestimos AS E
INNER JOIN tb_membros as M
ON E.id_membroE = M.id_membro
INNER JOIN tb_livros AS L
ON E.id_livroE = L.id_livro;

-- 4. Liste todos os empréstimos com o nome do membro, título do livro, nome do autor e data de devolução.
SELECT E.data_emprestimo AS 'Data de Empréstimo', M.nome AS 'Nome do Membro', L.titulo AS 'Titulo do Livro', A.nome AS 'Nome do Autor', E.data_devolucao AS 'Data Devolucao' FROM tb_emprestimos AS E
INNER JOIN tb_membros AS M
ON E.id_membroE = M.id_membro
INNER JOIN tb_livros AS L
ON E.id_livroE = L.id_livro
INNER JOIN tb_autores AS A
ON A.id_autor = L.id_autorL;

-- LEFT JOIN
-- 5. Liste todos os membros e, caso existam, os livros que eles já emprestaram.
SELECT M.nome AS 'Nome do Membro', L.titulo AS 'Titulo do Livro' FROM tb_emprestimos AS E
LEFT JOIN tb_membros AS M
ON E.id_membroE = M.id_membro
LEFT JOIN tb_livros AS L
ON E.id_livroE = L.id_livro;

-- 6. Liste todos os autores e os livros que eles escreveram (mesmo que algum autor ainda não tenha livros cadastrados).
SELECT A.nome AS 'Nome do Autor', L.titulo 'Titulo do Livro' FROM tb_autores as A 
LEFT JOIN tb_livros as L
ON L.id_autorL = A.id_autor;

-- RIGHT JOIN
-- 7. Liste todos os livros e, caso tenham, o nome do autor correspondente.
SELECT L.titulo AS 'Titulo do Livro', A.nome AS 'Nome do Autor' FROM tb_livros AS L
RIGHT JOIN tb_autores AS A
ON L.id_autorL = A.id_autor;

-- 8. Liste todos os livros e, caso tenham, os membros que os emprestaram.
SELECT L.titulo AS 'Titulo do Livro', M.nome AS 'Nome do Membro'  FROM tb_emprestimos as E
RIGHT JOIN tb_livros AS L
ON E.id_livroE = L.id_livro
RIGHT JOIN tb_membros AS M
ON E.id_membroE = M.id_membro;
