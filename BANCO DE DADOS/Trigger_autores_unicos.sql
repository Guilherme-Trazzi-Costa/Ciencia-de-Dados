CREATE DEFINER=`root`@`localhost` TRIGGER `Autores unicos` BEFORE INSERT ON `tb_autores` FOR EACH ROW BEGIN
	-- Se o autor existe
    IF EXISTS (SELECT 1 FROM tb_autores WHERE LOWER(nome) = LOWER(NEW.nome)) THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Autor já cadastrado !';
	END IF;
END