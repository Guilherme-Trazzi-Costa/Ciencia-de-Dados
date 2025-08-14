USE db_carro;

SELECT * FROM tb_carro;
INSERT INTO tb_carro (id_carro, marca, modelo, ano, valor,cor,numero_vendas) VALUES (
'1',
'Renault',
'Kwid',
'2023',
'80000',
'branco',
'150000'
);

INSERT INTO tb_carro(id_carro, marca, modelo, ano, valor, cor, numero_vendas) VALUES(
'2',
'Honda',
'Civic',
'2022',
'85000',
'prata',
'350000'
);

INSERT INTO tb_carro(id_carro, marca, modelo, ano, valor, cor, numero_vendas) VALUES(
'3',
'Fiat',
'Uno',
'2021',
'70000',
'preto',
'210000'
);

INSERT INTO tb_carro(id_carro, marca, modelo, ano, valor, cor, numero_vendas) VALUES(
'4',
'Chevrolet',
'Onix',
'2023',
'85000',
'azul',
'340000'
);

INSERT INTO tb_carro(id_carro, marca, modelo, ano, valor, cor, numero_vendas) VALUES(
'5',
'Fiat',
'Mobi',
'2022',
'72000',
'branco',
'310000'
);

INSERT INTO tb_carro(id_carro, marca, modelo, ano, valor, cor, numero_vendas) VALUES(
'6',
'Chevrolet',
'Cruze',
'2024',
'95000',
'chumbo',
'220000'
);

SELECT * FROM tb_proprietario;
INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
'1',
'Jessica',
'1',
'25'
);


INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
'2',
'Guilherme',
'2',
'25'
);

INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
'3',
'José',
'3',
'34'
);

INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
'4',
'Maria',
'4',
'29'
);

INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
'5',
'João',
'5',
'44'
);

INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
'6',
'Ana',
'6',
'25'
);

/*Alteração - UPDATE */
UPDATE tb_proprietario SET Idade = '23' WHERE id_proprietario = '6';

/* Visualizar linha especifica*/
SELECT * FROM tb_proprietario WHERE id_proprietario = '6';


SELECT * FROM tb_carro WHERE id_carro = '5';
UPDATE tb_carro SET valor = '70000' WHERE id_carro = '5';

SELECT * FROM tb_carro WHERE id_carro = '3';
UPDATE tb_carro SET valor = '75000' WHERE 	id_carro = '3';

SELECT * FROM tb_carro WHERE id_carro = '6';
UPDATE tb_carro SET numero_vendas = '240000' WHERE id_carro = '6';

SELECT * FROM tb_carro WHERE id_carro = '2';
UPDATE tb_carro SET cor = 'preto' WHERE	id_carro = '2';

SELECT * FROM tb_proprietario WHERE id_proprietario = '6';
UPDATE tb_proprietario SET nome = 'Ana', idade = '27' WHERE id_proprietario = '6';

SELECT * FROM tb_proprietario WHERE id_proprietario = '2';
DELETE FROM tb_proprietario WHERE id_proprietario = '2';


