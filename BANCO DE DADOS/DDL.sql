/* Criação base de dados */
CREATE DATABASE db_carro;

/* Acesso a base de dados */
USE db_carro;

/* Criação tabela */
CREATE TABLE tb_carro (
id_carro INT(10) NOT NULL,
marca VARCHAR(100),
modelo VARCHAR(100),
ano INT(4),
valor DECIMAL(10,2),
cor VARCHAR(100),
numero_vendas INT(10),
PRIMARY KEY (id_carro)
);

CREATE TABLE tb_proprietario(
id_proprietario INT(10) NOT NULL,
nome VARCHAR(255),
id_carroF INT(10) NOT NULL,
PRIMARY KEY(id_proprietario),
FOREIGN KEY(id_carroF) REFERENCES tb_carro(id_carro)
);

/* Alterar informações*/
ALTER TABLE tb_proprietario ADD idade INT(3);
ALTER TABLE tb_proprietario DROP idade; /* Remove coluna */
ALTER TABLE tb_proprietario RENAME COLUMN nome TO name; /* Remove coluna */
/*ALTER TABLE tb_proprietario CHANGE idade FLOAT(10,2);*/

SELECT marca, modelo FROM  tb_carro;
SELECT * FROM tb_proprietario;


CREATE TABLE tb_historico (
id_historico INT(10) NOT NULL,
data_modificacao DATE,
id_carro INT(10) NOT NULL,
valor_anterior DECIMAL(10,2),
valor_novo DECIMAL(10,2),
PRIMARY KEY (id_historico),
FOREIGN KEY (id_carro) REFERENCES tb_carro(id_carro)
)

/*Exclui tabela*/
/*DROP TABLE tb_historico;*/

SELECT * FROM tb_historico;

/*DROP TABLE tb_proprietario;*/



