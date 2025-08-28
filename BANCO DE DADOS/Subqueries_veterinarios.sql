USE ClinicaVetBD;


-- 1. Liste o nome e a data de nascimento do pet mais antigo da clínica usando uma subquery.
SELECT nome, data_nascimento FROM tb_pets
WHERE data_nascimento = (SELECT MIN(data_nascimento) FROM tb_pets)
ORDER BY data_nascimento ASC LIMIT 1;

-- 2. Liste o nome e a data de nascimento do pet mais novo usando uma subquery.
SELECT nome, data_nascimento FROM tb_pets
WHERE data_nascimento = (SELECT max(data_nascimento) FROM tb_pets)
ORDER BY data_nascimento ASC LIMIT 1;

-- 3. Liste o nome de todos os veterinários que realizaram atendimentos na data mais recente registrada.
SELECT V.nome, A.data_atendimento FROM tb_atendimentos AS A
INNER JOIN tb_veterinarios AS V
ON A.id_veterinarioA = V.id_veterinario
WHERE data_atendimento = (SELECT MAX(data_atendimento) FROM tb_atendimentos)
ORDER BY data_atendimento ASC LIMIT 1;


-- 4. Liste os nomes dos clientes que possuem mais de um pet, utilizando uma subquery para contar a quantidade.
SELECT C.nome
FROM tb_clientes AS C
WHERE (SELECT COUNT(id_pet) FROM tb_pets AS P
WHERE P.id_clienteP = C.id_cliente) > 1;
    
-- 5. Liste o nome de todos os pets que ainda não passaram por atendimento, utilizando uma subquery para verificar.
SELECT P.nome
FROM tb_pets AS P
WHERE (SELECT COUNT(id_petA) FROM tb_atendimentos AS A
	WHERE P.id_pet = A.id_petA) = 0;

-- 6. Para cada cliente, mostre o nome e a quantidade de pets cadastrados, utilizando uma subquery no SELECT.
SELECT C.nome, COUNT(P.id_pet) AS Numero_de_Pets
FROM tb_clientes AS C
INNER JOIN tb_pets AS P
ON P.id_clienteP = C.id_cliente
GROUP BY C.id_cliente;

-- OUTRO MODO DE FAZER
SELECT C.nome, 
(SELECT COUNT(*) FROM tb_pets AS P WHERE P.id_clienteP = C.id_cliente) AS 'Numero de pets'
FROM tb_clientes AS C;

-- 7. Liste todos os atendimentos realizados pelo veterinário mais recentemente cadastrado no sistema.
SELECT V.nome, A.id_atendimento, A.data_atendimento
FROM tb_atendimentos AS A
INNER JOIN tb_veterinarios AS V
ON A.id_veterinarioA = V.id_veterinario
WHERE V.id_veterinario = (
SELECT V2.id_veterinario
FROM tb_veterinarios AS V2
ORDER BY V2.id_veterinario DESC
LIMIT 1);


-- OUTRO MODO DE FAZER 
SELECT * FROM tb_atendimentos
WHERE id_veterinarioA = (SELECT MAX(id_veterinarioA) FROM tb_veterinarios);


-- 8. Liste todas as informações do atendimento mais antigo registrado, usando uma subquery para identificar a data.
SELECT * FROM tb_atendimentos AS A
WHERE A.data_atendimento = (SELECT MIN(data_atendimento) FROM tb_atendimentos);

-- 9. Clientes que já foram atendidos por mais de um veterinário diferente:
-- Liste os nomes dos clientes que já tiveram atendimentos com pelo
-- menos dois veterinários distintos, usando subquery.
    
SELECT C.nome
FROM tb_clientes AS C
WHERE (
SELECT COUNT( DISTINCT A.id_veterinarioA)
FROM tb_atendimentos AS A
INNER JOIN tb_pets AS P
ON A.id_petA = P.id_pet
WHERE P.id_clienteP = C.id_cliente) >= 2;

-- 10. Pets atendidos pelo veterinário mais solicitado:
-- Liste os nomes dos pets que foram atendidos pelo veterinário que mais
-- realizou atendimentos na clínica, usando subquery para identificar esse veterinário.

SELECT V.nome
FROM tb_veterinarios AS V
WHERE V.id_veterinario = (
    SELECT A.id_veterinarioA
    FROM tb_atendimentos AS A
    GROUP BY A.id_veterinarioA
    ORDER BY COUNT(*) ASC
    LIMIT 1
);

