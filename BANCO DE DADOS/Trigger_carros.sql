use db_carro;

update tb_carro set valor = 55000 where id_carro = '3';

select * from tb_historico;
select * from tb_carro;


ALTER TABLE tb_carro
MODIFY id_carro INT AUTO_INCREMENT;

select * from tb_carro;

UPDATE tb_carro SET valor = 900 WHERE id_carro = '2';

ALTER TABLE tb_proprietario
ADD data_nascimento date;

SELECT * FROM tb_proprietario;


INSERT INTO tb_proprietario
VALUES('8', 'Ricardo', '3', NULL, '2000/01/01');