USE db_academico;

-- DQL

-- Exercício 1: Liste todos os estudantes cadastrados na tabela estudantes que pertencem ao curso de TECNOLOGIA DA INFORMAÇÃO e foram matriculados em 2024.

SELECT * FROM estudantes;

SELECT E.nome, C.nome, E.data_matricula FROM tb_estudantes AS E
LEFT JOIN tb_cursos AS C
ON E.id_curso = C.id_curso
WHERE C.nome = 'Tecnologia da Informação' AND data_matricula <= '2024-12-31';

-- Exercício 2: Liste todos os professores que pertencem ao departamento de TECNOLOGIA DA INFORMAÇÃO e possuem mais de 5 anos de experiência.
SELECT nome, data_admissao FROM tb_professores
WHERE timestampdiff(YEAR, data_admissao, CURDATE()) >= 5;


-- Exercício 3: Liste os nomes dos estudantes e suas notas nas disciplinas, ordenadospela nota em ordem decrescente e, em caso de empate, pelo nome do estudanteem ordem alfabética.

SELECT E.nome, D.nome, N.nota FROM tb_matriculas AS M
RIGHT JOIN tb_estudantes AS E
ON M.id_estudante = E.id_estudante
INNER JOIN tb_notas AS N
ON M.id_matricula = N.id_matricula
INNER JOIN tb_disciplinas AS D
ON D.id_disciplina = M.id_disciplina
ORDER BY N.nota DESC, D.nome ASC;

-- Exercício 4: Encontre a média das notas dos estudantes no curso de DIREITO.
SELECT AVG(nota) FROM tb_matriculas AS M
INNER JOIN tb_notas AS N
ON M.id_matricula = N.id_matricula
INNER JOIN tb_estudantes AS E
ON M.id_estudante = E.id_estudante
INNER JOIN tb_cursos AS C
ON E.id_curso = C.id_curso
WHERE C.nome = 'Direito';

-- Exercício 5: Liste os cursos que possuem mais de 50 estudantes matriculados. Exiba o nome do curso e o total de estudantes matriculados.
SELECT C.nome, COUNT(C.id_curso) AS Qtd
FROM tb_cursos AS C
GROUP BY C.nome
HAVING COUNT(C.id_curso) > 5;

-- SUBQUERYES

-- Exercício 1: Liste os cursos que possuem mais de 5 disciplinas associadas.
SELECT C.nome FROM tb_cursos AS C
LEFT JOIN tb_disciplinas AS D
ON C.id_curso = D.id_curso
GROUP BY C.nome
HAVING COUNT(D.id_disciplina)> 5;

-- Exercício 2: Liste os estudantes que estão matriculados em mais disciplinas do que a média de disciplinas por estudante.
SELECT E.nome FROM tb_estudantes AS E
INNER JOIN tb_cursos AS C
ON E.id_curso = C.id_curso
INNER JOIN tb_disciplinas AS D
ON D.id_disciplina = C.id_disciplina
HAVING COUNT(id_disciplinas) > (SELECT AVG(D.id_disciplina) FROM tb_disciplinas);






