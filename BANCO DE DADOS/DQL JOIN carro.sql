USE db_carro;


-- INNER JOIN
SELECT * FROM tb_proprietario AS P
INNER JOIN tb_carro AS C
ON P.id_carroF = C.id_carro;

-- LEFT JOIN
SELECT * FROM tb_proprietario AS P
LEFT JOIN tb_carro AS C
ON P.id_carroF = C.id_carro;

-- RIGHT JOIN
SELECT * FROM tb_proprietario AS P
RIGHT JOIN tb_carro AS C
ON P.id_carroF = C.id_carro;

-- FULL JOIN OU UNION
SELECT * FROM tb_proprietario AS P
UNION tb_carro AS C
ON P.id_carroF = C.id_carro;