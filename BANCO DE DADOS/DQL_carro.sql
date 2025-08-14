USE db_carro;

SELECT * FROM tb_carro;
SELECT modelo, cor FROM tb_carro;
SELECT * FROM tb_carro WHERE cor = 'preto';

SELECT * FROM tb_carro WHERE modelo = 'Civic';

SELECT min(valor) FROM tb_carro;

SELECT max(ano) FROM tb_carro;

SELECT COUNT(cor) FROM tb_carro;

SELECT * FROM tb_carro ORDER BY modelo ASC;

SELECT * FROM tb_carro ORDER BY marca DESC;

-- INFORMAR QUANTIDADE DE REGISTROS DE MARCA QUE ESTÁ ENTRE UM PERÍODO DE TEMPO

SELECT COUNT(id_carro) AS 'TOTAL REGISTROS', marca 
FROM tb_carro 
WHERE ano 
between 2020 AND 2024 GROUP BY marca;



SELECT COUNT(id_carro) AS 'REGISTRO NO ANO DE 2023', marca
FROM tb_carro
WHERE ano = '2023'
GROUP BY marca;


