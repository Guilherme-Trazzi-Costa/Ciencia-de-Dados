CREATE DEFINER=`root`@`localhost` TRIGGER `tb_carro_AFTER_UPDATE` AFTER UPDATE ON `tb_carro` FOR EACH ROW BEGIN
	IF NEW.valor <> OLD.valor THEN
		INSERT INTO tb_historico VALUES (null, now(), new.id_carro, old.valor, new.valor);
	END IF;
END