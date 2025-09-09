CREATE DATABASE db_plataforma;

USE db_plataforma;

CREATE TABLE eventos(
id INT UNIQUE NOT NULL auto_increment PRIMARY KEY,
titulo VARCHAR(100),
categoria VARCHAR(100),
detalhes JSON,
inscricoes JSON
);



INSERT INTO eventos (titulo, categoria, detalhes, inscricoes) VALUES
(
  "Palestra de Carreiras",
  "Carreiras",
  '{"local":"Santo André", "data":"2025-07-05", "palestrantes":["José Carlos"]}',
  '[{"nome":"Felipe","email":"felipe@email.com","presente":true}, {"nome":"Maria","email":"maria@email.com","presente":false}]'
),
(
  "Palestra de Vida e Saúde",
  "Vida e Saúde",
  '{"local":"São Caetano do Sul", "data":"2025-08-23", "palestrantes":["Gilson Kleina"]}',
  '[{"nome":"Gabriel","email":"gabriel@email.com","presente":true}, {"nome":"Lilian","email":"lilian@email.com","presente":true}]'
),
(
  "Workshop Financeiro",
  "Economia",
  '{"local":"São Bernardo do Campo", "data":"2025-03-15", "palestrantes":["João Geremaia","Ana Carolina"]}',
  '[{"nome":"Gustavo","email":"gustavo@email.com","presente":true}, {"nome":"Thiago","email":"thi@email.com","presente":true}]'
),
(
  "Workshop IoT",
  "Tecnologia",
  '{"local":"São Paulo", "data":"2025-05-17", "palestrantes":["Lucio Augusto Filho"]}',
  '[{"nome":"Leonardo","email":"leo@email.com","presente":true}, {"nome":"Katia","email":"katia@email.com","presente":false}, {"nome":"Eduardo","email":"edu@email.com","presente":true}, {"nome":"Gabriela","email":"gabi@email.com","presente":true}]'
),
(
  "Palestra de Redes Sociais",
  "Tecnologia",
  '{"local":"São Paulo", "data":"2025-03-23", "palestrantes":["Barbara Alencar"]}',
  '[{"nome":"Mateus","email":"mat@email.com","presente":true}, {"nome":"Beatriz","email":"Bia@email.com","presente":true}, {"nome":"Ana","email":"aninha@email.com","presente":true}, {"nome":"Giovanna","email":"gio@email.com","presente":false}]'
);

SELECT titulo FROM eventos
WHERE JSON_CONTAINS(detalhes -> '$.palestrantes','"Barbara Alencar"');


SELECT 
    titulo,
    JSON_EXTRACT(inscricoes, '$[*].nome')   AS Nomes,
    JSON_EXTRACT(inscricoes, '$[*].presente') = true AS Presenca
FROM eventos;

SELECT	
JSON_EXTRACT(detalhes, '$.palestrantes') AS Palestrante,
JSON_EXTRACT(detalhes, '$.local') AS Local
FROM eventos;

SELECT 
    titulo,
    JSON_EXTRACT(inscricoes, '$[*].nome')   AS Nomes,
    JSON_EXTRACT(inscricoes, '$[*].presente') = False AS Presenca
FROM eventos;

SELECT 
    titulo,
    JSON_EXTRACT(inscricoes, '$[*].nome')   AS Nomes,
    JSON_EXTRACT(inscricoes, '$[*].presente') = false AS Presenca
FROM eventos;