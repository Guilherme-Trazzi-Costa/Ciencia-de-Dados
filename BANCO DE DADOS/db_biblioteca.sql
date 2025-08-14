CREATE DATABASE db_biblioteca;

USE db_biblioteca;

CREATE TABLE tb_autores(
id_autor INT(10) NOT NULL UNIQUE,
nome VARCHAR(255),
data_nascimento DATE,
PRIMARY KEY(id_autor)
);

CREATE TABLE tb_livros(
id_livro INT(10) NOT NULL UNIQUE,
titulo VARCHAR(255),
ano_publicacao INT(4),
id_autorL INT(10) NOT NULL,
PRIMARY KEY(id_livro),
FOREIGN KEY(id_autorL) REFERENCES tb_autores(id_autor)
);


SELECT * FROM tb_livros;

CREATE TABLE tb_membros(
id_membro INT(10) NOT NULL UNIQUE,
nome VARCHAR(255),
data_adesao DATE,
PRIMARY KEY(id_membro)
);

SELECT * FROM tb_membros;

CREATE TABLE tb_emprestimos(
id_emprestimo INT(10) NOT NULL UNIQUE,
id_membroE INT(10) NOT NULL UNIQUE,
id_livroE INT(10) NOT NULL UNIQUE,
data_emprestimo DATE,
data_devolucao DATE,
PRIMARY KEY(id_emprestimo),
FOREIGN KEY(id_membroE) REFERENCES tb_membros(id_membro),
FOREIGN KEY(id_livroE) REFERENCES tb_livros(id_livro)
);

ALTER TABLE tb_emprestimos RENAME COLUMN id_membro TO id_membroE;
SELECT * FROM tb_emprestimos;