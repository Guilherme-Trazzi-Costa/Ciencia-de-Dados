USE clinicavetbd;

SELECT * FROM tb_atendimentos;
SELECT *FROM tb_veterinarios;

INSERT INTO tb_veterinarios VALUES(
'4',
'Hugo',
'Dermatologista',
'1234-5456'
);

SELECT * FROM tb_atendimentos AS A
INNER JOIN tb_veterinarios AS V
ON A.id_veterinarioA = V.id_veterinario;

SELECT * FROM tb_atendimentos AS A
LEFT JOIN tb_veterinarios AS V
ON A.id_veterinarioA = V.id_veterinario;

SELECT * FROM tb_veterinarios AS V
LEFT JOIN tb_atendimentos AS A
ON V.id_veterinario = A.id_veterinarioA;

SELECT * FROM tb_veterinarios AS V
RIGHT JOIN tb_atendimentos AS A
ON V.id_veterinario = A.id_veterinarioA;

SELECT P.nome AS 'Nome pet', C.nome AS 'Nome cliente', C.telefone FROM tb_pets AS P
INNER JOIN tb_clientes AS C
ON P.id_clienteP = C.id_cliente;

SELECT C.nome, P.nome FROM tb_clientes AS C
LEFT JOIN tb_pets AS P
ON C.id_cliente = P.id_clienteP;

SELECT A.id_atendimento, A.data_atendimento, V.nome FROM tb_veterinarios AS V
RIGHT JOIN tb_atendimentos AS A
ON V.id_veterinario = A.id_veterinarioA;

