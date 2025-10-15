CREATE DATABASE db_projetos;

use db_projetos;
CREATE TABLE tb_litoral (
    id INT AUTO_INCREMENT PRIMARY KEY,
    localizacao VARCHAR(200),
    dia_hora VARCHAR(200),
    co2 DECIMAL(20,2),
    poeira_1 DECIMAL(20,2),
    poeira_2 DECIMAL(20,2),
    pressao DECIMAL(20,2),
    umidade DECIMAL(20,2),
    temperatura DECIMAL(20,2),
    altitude DECIMAL(20,2)
);

DROP TABLE tb_litoral;
SELECT * FROM tb_litoral;

CREATE TABLE tb_adicional(
id_adicional INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
qualidade_ar DECIMAL(20,2),
densidade_ar DECIMAL(20,2),
velocidade_vento DECIMAL(20,2),
previsao_chuva DECIMAL(20,2),
id INT NOT NULL,
FOREIGN KEY (id) REFERENCES tb_litoral(id)
);

DROP TABLE tb_adicional;
SELECT * FROM tb_adicional;
