USE db_biblioteca;

SELECT * FROM tb_autores;

INSERT INTO tb_autores(id_autor, nome, data_nascimento) VALUES(
'1',
'Abel',
'1975/03/22'
);

INSERT INTO tb_autores(id_autor, nome, data_nascimento) VALUES(
'2',
'Breno',
'1988-05-11'
);

INSERT INTO tb_autores(id_autor, nome, data_nascimento) VALUES(
'3',
'Charles',
'1965-06-2'
);

INSERT INTO tb_autores(id_autor, nome, data_nascimento) VALUES(
'4',
'Diana',
'1968-09-28'
);

INSERT INTO tb_autores(id_autor, nome, data_nascimento) VALUES(
'5',
'Eliana',
'1979-12-17'
);


SELECT * FROM tb_livros;

INSERT INTO tb_livros(id_livro, titulo, ano_publicacao, id_autorL) VALUES(
'1',
'A história de Abel',
'2022',
'1'
);

INSERT INTO tb_livros(id_livro, titulo, ano_publicacao, id_autorL) VALUES(
'2',
'Breno o Mago',
'2020',
'2'
);

INSERT INTO tb_livros(id_livro, titulo, ano_publicacao, id_autorL) VALUES(
'3',
'O Charles Magno',
'2017',
'3'
);

INSERT INTO tb_livros(id_livro, titulo, ano_publicacao, id_autorL) VALUES(
'4',
'A Mulher Diana',
'2005',
'4'
);

INSERT INTO tb_livros(id_livro, titulo, ano_publicacao, id_autorL) VALUES(
'5',
'A Estrela Eliana',
'2000',
'5'
);


SELECT * FROM tb_membros;

INSERT INTO tb_membros(id_membro, nome, data_adesao) VALUES(
'1',
'Ana',
'2025-05-15'
);

INSERT INTO tb_membros(id_membro, nome, data_adesao) VALUES(
'2',
'Beatriz',
'2025-02-04'
);

INSERT INTO tb_membros(id_membro, nome, data_adesao) VALUES(
'3',
'Camilo',
'2025-03-22'
);

INSERT INTO tb_membros(id_membro, nome, data_adesao) VALUES(
'4',
'Diego',
'2025-06-10'
);

INSERT INTO tb_membros(id_membro, nome, data_adesao) VALUES(
'5',
'Eusébio',
'2025-01-27'
);


SELECT * FROM tb_emprestimos;

INSERT INTO tb_emprestimos(id_emprestimo, id_membroE, id_livroE, data_emprestimo, data_devolucao) VALUES(
'1',
'1',
'1',
'2025-05-15',
'2025-5-22'
);

INSERT INTO tb_emprestimos(id_emprestimo, id_membroE, id_livroE, data_emprestimo, data_devolucao) VALUES(
'2',
'2',
'2',
'2025-02-04',
'2025-02-11'
);

INSERT INTO tb_emprestimos(id_emprestimo, id_membroE, id_livroE, data_emprestimo, data_devolucao) VALUES(
'3',
'3',
'3',
'2025-03-22',
'2025-03-29'
);

INSERT INTO tb_emprestimos(id_emprestimo, id_membroE, id_livroE, data_emprestimo, data_devolucao) VALUES(
'4',
'4',
'4',
'2025-06-10',
'2025-06-17'
);

INSERT INTO tb_emprestimos(id_emprestimo, id_membroE, id_livroE, data_emprestimo, data_devolucao) VALUES(
'5',
'5',
'5',
'2025-01-27',
'2025-02-03'
);


SELECT * FROM tb_autores;
UPDATE tb_autores SET data_nascimento = '1965-06-06' WHERE id_autor = 3;

SELECT * FROM tb_autores WHERE id_autor = '2';
UPDATE tb_autores SET nome = 'Brito' WHERE id_autor = '2';

SELECT * FROM tb_livros WHERE id_livro = '3';
UPDATE tb_livros SET ano_publicacao = '2015' WHERE  id_livro = '3';

SELECT * FROM tb_membros WHERE id_membro = '5';
UPDATE tb_membros SET data_adesao = '2025-01-17' WHERE id_membro = '5';

SELECT * FROM tb_membros WHERE id_membro = '4';
UPDATE tb_membros SET nome = 'Diogo' WHERE id_membro = '4';

