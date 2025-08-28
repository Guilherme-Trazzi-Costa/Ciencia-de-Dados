CREATE DEFINER=`root`@`localhost` TRIGGER `Limitador idade` BEFORE INSERT ON `tb_autores` FOR EACH ROW BEGIN
	DECLARE idade_autor INT;
		SET NEW.idade = timestampdiff(YEAR, NEW.data_nascimento, curdate());
		
		SELECT idade INTO idade_autor FROM tb_autores;
		-- WHERE id_autor = NEW.id_autor AND idade < 18;
    
    IF idade_autor < 18 THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'O AUTOR NÃO PODE TER MENOS DE 18 ANOS';
    END IF;
END