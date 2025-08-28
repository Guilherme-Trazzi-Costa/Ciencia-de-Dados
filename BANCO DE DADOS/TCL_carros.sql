USE db_carro;

SELECT @@autocommit;

SET @@autocommit = OFF; -- DESATIVA O 'SALVAR AUTOMATICAMENTE'


SELECT * FROM tb_proprietario;

-- ROLLBACK SIMPLES
-- INSERT

START TRANSACTION;
	INSERT INTO tb_proprietario(id_proprietario, nome, id_carroF, idade) VALUES(
	'7',
	'Daniel',
	'5',
	'35'
	);
COMMIT;

ROLLBACK;
