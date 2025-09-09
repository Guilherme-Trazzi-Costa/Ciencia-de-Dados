CREATE DATABASE db_academico;

USE db_academico;

-- DDL
-- TABERLA CURSOS
CREATE TABLE tb_cursos(
id_curso INT NOT NULL UNIQUE,
nome VARCHAR(100) NOT NULL,
duracao_anos INT NOT NULL,
PRIMARY KEY(id_curso)
);

ALTER TABLE tb_cursos MODIFY COLUMN id_curso INT AUTO_INCREMENT;

-- TABELA PROFESSORES
CREATE TABLE tb_professores(
id_professor INT NOT NULL UNIQUE,
nome VARCHAR(100) NOT NULL,
departamento VARCHAR(100) NOT NULL,
ano_admissao INT NOT NULL,
PRIMARY KEY(id_professor)
);

ALTER TABLE tb_professores MODIFY COLUMN id_professor INT AUTO_INCREMENT;


-- TABELA DISCIPLINAS
CREATE TABLE tb_disciplinas(
id_disciplina INT NOT NULL UNIQUE,
nome VARCHAR(100) NOT NULL,
id_curso INT NOT NULL,
id_professor INT NOT NULL,
PRIMARY KEY(id_disciplina),
FOREIGN KEY(id_curso) REFERENCES tb_cursos(id_curso),
FOREIGN KEY(id_professor) REFERENCES tb_professores(id_professor)
);

ALTER TABLE tb_disciplinas MODIFY COLUMN id_disciplina INT AUTO_INCREMENT;


-- TABELA ESTUDANTES
CREATE TABLE tb_estudantes(
id_estudante INT NOT NULL UNIQUE,
nome VARCHAR(100) NOT NULL,
data_nascimento DATE NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
id_curso INT NOT NULL,
data_matricula DATE,
PRIMARY KEY(id_estudante),
FOREIGN KEY(id_curso) REFERENCES tb_cursos(id_curso)
);

ALTER TABLE tb_estudantes MODIFY COLUMN id_estudante INT AUTO_INCREMENT;

-- TABELA MATRICULAS
CREATE TABLE tb_matriculas(
id_matricula INT NOT NULL UNIQUE,
id_estudante INT NOT NULL UNIQUE,
id_disciplina INT NOT NULL,
data_matricula DATE NOT NULL,
PRIMARY KEY(id_matricula),
FOREIGN KEY(id_estudante) REFERENCES tb_estudantes(id_estudante),
FOREIGN KEY(id_disciplina) REFERENCES tb_disciplinas(id_disciplina)
);

drop table tb_matriculas;

ALTER TABLE tb_matriculas MODIFY COLUMN id_matricula INT AUTO_INCREMENT;


-- TABELA NOTAS
CREATE TABLE tb_notas(
id_nota INT UNIQUE,
id_matricula INT NOT NULL,
nota DECIMAL(5,2),
data_lançamento DATE
);

ALTER TABLE tb_notas MODIFY COLUMN id_nota INT AUTO_INCREMENT;

-- DML
-- Insira 5 novos registros de professores, cursos e disciplinas.

-- INSERÇÃO CURSOS
SELECT * FROM tb_cursos;
INSERT INTO tb_cursos VALUES
('1', 'Administração', 3),
('2', 'Nutrição', 3),
('3', 'Direito', 5),
('4', 'Medicina', 5),
('5', 'Tecnologia da Informação', 4);


-- INSERT PROFESSORES
SELECT * FROM tb_professores;
INSERT INTO tb_professores VALUES
('1', 'Carlos Silva', 'Administração e Negócios', '2005'),
('2', 'Ana Paula Souza', 'Saúde e Bem Estar', '2020'),
('3', 'José Almeida', 'Advocacia e Direito', '2000'),
('4', 'Maria Fernandes', 'Medicina e Saúde', '2017'),
('5', 'João Pereira', 'Tecnologia da Informação', '2022');

-- DAR INSERT
-- INSERÇÃO DISCIPLINAS
SELECT * FROM tb_disciplinas;
INSERT INTO tb_disciplinas VALUES
('1', 'Gestão e Negócios', '1', '1'),
('2', 'Ciência dos Alimentos', '2', '2'),
('3', 'Direito Constitucional', '3', '3'),
('4', 'Anatomia Humana', '4', '4'),
('5', 'Arquitetura de Dados', '5', '5');


-- INSERT ESTUDANTES
SELECT * FROM tb_estudantes;
INSERT INTO tb_estudantes VALUES
('1', 'Lucas Almeida', '2003-02-03', 'lucasalmeida@gmail.com', '1', '2023-01-02'),
('2', 'Mariana Ferreira', '2007-10-01', 'mariferreira@gamil.com', '2', '2025-02-12'),
('3', 'Rafael Souza', '2004-07-09','rafasouza@gmail.com','3', '2022-02-03'),
('4', 'Beatriz Oliveira', '2006-07-09','biaoliveira@gmail.com','4' ,'2021-01-20'),
('5', 'Gabriel Santos', '2007-03-22','gabrielsantoss@gmail.com', '5', '2024-03-02');

-- INSERT MATRICULAS
SELECT * FROM tb_matriculas;
INSERT INTO tb_matriculas VALUES
('1','1', '1', '2023-01-02'),
('2','2', '2', '2025-02-12'),
('3','3', '3', '2022-02-03'),
('4','4', '4', '2021-01-20'),
('5','5', '5', '2024-03-02');

-- INSERT NOTAS
SELECT * FROM tb_notas;
INSERT INTO tb_notas VALUES
('1', '1', '7.5', '2023-12-20'),
('2', '2', '8.7', '2025-06-23'),
('3', '3', '9.2', '2024-12-03'),
('4', '4', '5.7', '2022-07-23'),
('5','5', '6.4', '2024-07-12');

