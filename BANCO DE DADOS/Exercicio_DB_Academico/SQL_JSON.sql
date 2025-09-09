CREATE DATABASE empresa_xpto;

USE empresa_xpto;

CREATE TABLE clientes (
id INT NOT NULL UNIQUE auto_increment PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100),
preferencias JSON
);

SELECT * FROM clientes;

INSERT INTO clientes (nome, email, preferencias)
VALUES
("Felipe", "felipe@prof.com", '{"interesses": ["livros", "computação"], "notificações": true}'),
("Nicole", "nicole@gmail.com", '{"interesses": ["programação", "C#"], "notificações": false}');


SELECT * FROM clientes WHERE preferencias = '{"interesses": ["livros", "computação"], "notificações": true}';


SELECT nome FROM clientes
WHERE JSON_CONTAINS(preferencias -> '$.interesses','"livros"');

SELECT JSON_VALID('{"interesses": ["livros", "computação"], "notificações": true}');

-- Separa as colunas
SELECT nome, 
JSON_EXTRACT(preferencias, '$.interesses[0]')  AS interesses1,
JSON_EXTRACT(preferencias, '$.interesses[1]')  AS interesses2
FROM clientes
WHERE JSON_EXTRACT(preferencias, '$.notificações') = false;

SELECT nome, JSON_KEYS(preferencias) FROM clientes;
SELECT JSON_TYPE(preferencias-> '$.interesses[0]') FROM clientes;

UPDATE clientes 
SET preferencias = JSON_INSERT(preferencias, '$.premium', false)
WHERE id = '1'; -- criar o campo dentro do documento

-- JSON SET() - Atualiza um campo
-- JSON REMOVE(preferencias, '$.premium') - Remove Campo do documento
SELECT * FROM clientes;


-- -> substitui o JSON_EXTRACT
SELECT nome, 
preferencias-> '$.interesses[0]'  AS interesses1,
preferencias-> '$.interesses[1]'  AS interesses2
FROM clientes;


-- JSON_UNQUOTE - Remove aspas das informações
SELECT nome, 
JSON_UNQUOTE(preferencias-> '$.interesses[0]')  AS interesses1,
JSON_UNQUOTE(preferencias-> '$.interesses[1]')  AS interesses2
FROM clientes;


-- ->> também remove as aspas
SELECT nome, 
preferencias->> '$.interesses[0]'  AS interesses1,
preferencias->> '$.interesses[1]'  AS interesses2
FROM clientes;