USE db_carro;

-- CALCULAR A MÉDIA
SELECT AVG(valor) FROM tb_carros;

-- SELECT DOS CARROS COM PREÇO MAIOR QUE A MÉDIA
SELECT * FROM tb_carro WHERE valor > (SELECT AVG(valor) FROM tb_carro);


SELECT * FROM tb_carro WHERE marca = 'Fiat';

SELECT * FROM tb_proprietario WHERE id_carro = '3';

SELECT * FROM tb_proprietario AS P
WHERE id_carro IN (SELECT * FROM tb_carro WHERE marca = 'Fiat');


USE db_biblioteca;

SELECT AVG(ano_publicacao) FROM tb_livros;

SELECT * FROM tb_livros 
WHERE ano_publicacao > (SELECT AVG(ano_publicacao) FROM tb_livros);

USE clinicavetbd;
SELECT * FROM tb_clientes;
SELECT * FROM tb_pets;


SELECT * FROM tb_clientes WHERE id_clientes = '2';

SELECT id_clienteP FROM tb_pets GROUP BY id_clienteP HAVING COUNT(*) > 1;

SELECT * FROM tb_clientes WHERE id_cliente IN (SELECT id_clienteP FROM tb_pets GROUP BY id_clienteP HAVING COUNT(*) > 1);
