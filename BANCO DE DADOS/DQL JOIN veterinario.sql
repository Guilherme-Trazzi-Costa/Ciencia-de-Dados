USE ClinicaVetBD;

-- 1. Liste o nome do pet, o nome do cliente e o telefone do cliente para todos os pets cadastrados.
SELECT P.nome, C.nome, telefone FROM tb_pets AS P
INNER JOIN tb_clientes AS C
ON P.id_clienteP = C.id_cliente;

-- 2. Liste a data, a descrição do atendimento, o nome do pet e o nome do veterinário responsável.
SELECT A.data_atendimento, A.descricao, V.nome AS 'Nome Veterinario', P.nome AS 'Nome Pet' FROM tb_atendimentos as A
INNER JOIN tb_veterinarios AS V
ON A.id_veterinarioA = V.id_veterinario
INNER JOIN tb_pets AS P
ON A.id_petA = P.id_pet;

-- 3. Liste o nome do veterinário e todos os pets que ele já atendeu.
SELECT V.nome, P.nome  FROM tb_veterinarios AS V
INNER JOIN tb_atendimentos AS A
ON V.id_veterinario = A.id_veterinarioA
INNER JOIN tb_pets AS P
ON A.id_petA = P.id_pet;

-- 4. Mostre o nome do cliente, o nome do pet e a especialidade do veterinário para cada atendimento realizado.
SELECT C.nome AS 'Nome Cliente', P.nome AS 'Nome Pet', especialidade AS 'Especialidade Veterinario' FROM tb_veterinarios AS V
INNER JOIN tb_atendimentos as A
ON V.id_veterinario = A.id_veterinarioA
INNER JOIN tb_pets AS P
ON P.id_pet = A.id_petA
INNER JOIN tb_clientes AS C
ON C.id_cliente = P.id_clienteP;

-- LEFT JOIN
-- 5. Liste todos os clientes e, caso existam, seus respectivos pets (mesmo que não tenham atendimento registrado).
SELECT C.nome AS 'Nome Cliente', P.nome AS 'Nome Pet' FROM tb_pets as P
LEFT JOIN tb_clientes as C
ON C.id_cliente = P.id_clienteP;

-- 6. Liste todos os veterinários e, caso existam, os atendimentos realizados por eles.
SELECT V.nome AS 'Nome Veterinario', A.data_atendimento FROM tb_veterinarios AS V
LEFT JOIN tb_atendimentos AS A
ON V.id_veterinario = A.id_veterinarioA;

-- RIGHT JOIN
-- 7. Liste todos os pets e, caso existam, seus respectivos donos (mesmo que alguns registros de clientes não existam).
SELECT P.nome AS 'Nome Pet', C.nome AS 'Nome Cliente'FROM tb_pets AS P
RIGHT JOIN tb_clientes AS C
ON P.id_clienteP = C.id_cliente;

-- 8. Liste todos os atendimentos, mesmo que algum veterinário não esteja cadastrado na tabela.
SELECT A.data_atendimento, V.nome AS 'Nome Veterinario' FROM tb_atendimentos as A
RIGHT JOIN tb_veterinarios AS V
ON A.id_veterinarioA = V.id_veterinario;