-- EXERCICIO 1. Criação do Banco de Dados
CREATE DATABASE ClinicaVetBD;

USE ClinicaVetBD;

-- EXERCICIO 2. Criação das Tabelas
CREATE TABLE tb_veterinarios (
id_veterinario INT(10) NOT NULL UNIQUE,
nome VARCHAR(255),
especialidade VARCHAR(255),
telefone VARCHAR(25),
PRIMARY KEY(id_veterinario)
);

CREATE TABLE tb_clientes (
id_cliente INT(10) NOT NULL UNIQUE,
nome VARCHAR(255),
endereco VARCHAR(255),
telefone VARCHAR(25),
PRIMARY KEY(id_cliente)
);

CREATE TABLE tb_pets (
id_pet INT(10) NOT NULL UNIQUE,
nome VARCHAR(255),
tipo VARCHAR(255),
raca VARCHAR(255),
data_nascimento DATE,
id_clienteP INT(10) NOT NULL UNIQUE,
PRIMARY KEY(id_pet),
FOREIGN KEY(id_clienteP) REFERENCES tb_clientes(id_cliente)
);

CREATE TABLE tb_atendimentos (
id_atendimento INT(10) NOT NULL UNIQUE,
id_petA INT(10) NOT NULL UNIQUE,
id_veterinarioA INT(10) NOT NULL,
data_atendimento DATE,
descricao VARCHAR(255),
PRIMARY KEY(id_atendimento),
FOREIGN KEY(id_petA) REFERENCES tb_pets(id_pet),
FOREIGN KEY(id_veterinarioA) REFERENCES tb_veterinarios(id_veterinario)
);

-- EXERCICIO 3. Inserir ao menos 3 valores em cada tabela
SELECT * FROM tb_veterinarios;
INSERT INTO tb_veterinarios ( id_veterinario, nome, especialidade, telefone) VALUES(
'1',
'Ana',
'Pneumologista',
'1111-2222'
);

INSERT INTO tb_veterinarios (id_veterinario, nome, especialidade, telefone) VALUES(
'2',
'Bartolomeu',
'Clinico Geral',
'1212-2121'
);

INSERT INTO tb_veterinarios (id_veterinario, nome, especialidade, telefone) VALUES(
'3',
'Cleantes',
'Oftalmologista',
'1231-2132'
);

SELECT * FROM tb_clientes;
INSERT INTO tb_clientes (id_cliente, nome, endereco, telefone) VALUES(
'1',
'Alberto',
'São Caetano do Sul',
'2134-3421'
);

INSERT INTO tb_clientes (id_cliente, nome, endereco, telefone) VALUES(
'2',
'Claudia',
'Santo André',
'3124-4231'
);

INSERT INTO tb_clientes (id_cliente, nome, endereco, telefone) VALUES(
'3',
'Cirio',
'São Bernardo do Campo',
'4231-1324'
);


SELECT * FROM tb_pets;
INSERT INTO tb_pets (id_pet, nome, tipo, raca, data_nascimento, id_clienteP) VALUES(
'1',
'Max',
'Cachorro',
'Pastor Alemão',
'2015-10-22',
'1'
);

INSERT INTO tb_pets (id_pet, nome, tipo, raca, data_nascimento, id_clienteP) VALUES(
'2',
'Maya',
'Gata',
'Persa',
'2017-03-15',
'2'
);

INSERT INTO tb_pets (id_pet, nome, tipo, raca, data_nascimento, id_clienteP) VALUES(
'3',
'Pipo',
'Passaro',
'Calopsita',
'2021-06-16',
'3'
);

INSERT INTO tb_pets (id_pet, nome, tipo, raca, data_nascimento, id_clienteP) VALUES(
'4',
'Baro',
'Passaro',
'Calopsita',
'2021-06-16',
'3'
);


SELECT * FROM tb_atendimentos;
INSERT INTO tb_atendimentos (id_atendimento, id_petA, id_veterinarioA, data_atendimento, descricao) VALUES(
'1',
'1',
'1',
'2025-06-09',
'Cachorro apresentava falta de ar e cansaço, após raio-x foi identificado pneumonia leve'
);

INSERT INTO tb_atendimentos (id_atendimento, id_petA, id_veterinarioA, data_atendimento, descricao) VALUES(
'2',
'2',
'3',
'2025-03-19',
'Gata apresentava secreções nos olhos, possível infecção'
);

INSERT INTO tb_atendimentos (id_atendimento, id_petA, id_veterinarioA, data_atendimento, descricao) VALUES(
'3',
'3',
'2',
'2025-02-25',
'Passaro não está se alimentando e fica encolhido no canto da gaiola, possível resfriado'
);

INSERT INTO tb_atendimentos (id_atendimento, id_petA, id_veterinarioA, data_atendimento, descricao) VALUES(
'4',
'4',
'3',
'2025-02-27',
'Passaro está com secreções nos olhos, possível resfriado'
);

-- EXERCICIO 4. Realize ao menos 5 alterações (UPDATES)
SELECT * FROM tb_veterinarios WHERE id_veterinario = '2';
UPDATE tb_veterinarios SET nome = 'Bryan' WHERE id_veterinario = '2';

SELECT * FROM tb_clientes WHERE id_cliente = '3';
UPDATE tb_clientes SET endereco = 'São Paulo' WHERE id_cliente = '3';

SELECT * FROM  tb_pets WHERE id_pet = '3';
UPDATE tb_pets SET nome = 'Bipo' WHERE id_pet = '3';

SELECT * FROM tb_atendimentos WHERE id_atendimento = '1';
UPDATE tb_atendimentos SET data_atendimento = '2025-09-06' WHERE id_atendimento = '1';

SELECT * FROM tb_clientes WHERE id_cliente = '1';
UPDATE tb_clientes SET nome = 'Adalberto' WHERE id_cliente = '1';

UPDATE tb_veterinarios SET nome = 'Ana' WHERE id_veterinario = '2';

-- EXERCICIO 5. Realize as seguintes consultas:
SELECT nome, data_nascimento FROM tb_pets ORDER BY data_nascimento ASC LIMIT 1;

SELECT nome, data_nascimento FROM tb_pets ORDER BY data_nascimento DESC LIMIT 1;

SELECT COUNT(id_pet) FROM tb_pets;

SELECT * FROM tb_pets ORDER BY nome ASC;

SELECT * FROM tb_pets ORDER BY nome DESC;

SELECT * FROM tb_veterinarios ORDER BY nome ASC;

SELECT * FROM tb_veterinarios ORDER BY nome DESC;

SELECT * FROM tb_atendimentos ORDER BY data_atendimento ASC LIMIT 1;

SELECT * FROM tb_atendimentos ORDER BY data_atendimento DESC LIMIT 1;

