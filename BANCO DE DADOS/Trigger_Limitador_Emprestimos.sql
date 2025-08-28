CREATE DEFINER=`root`@`localhost` TRIGGER `tb_emprestimos_BEFORE_INSERT` BEFORE INSERT ON `tb_emprestimos` FOR EACH ROW BEGIN
	DECLARE total_emprestimos INT;
    
    SELECT COUNT(*) INTO total_emprestimos FROM tb_emprestimos
    WHERE id_membroe = NEW.id_membroE AND data_devolucao > NOW();
    
    IF total_emprestimos >= 3 THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'O MEMBRO NÃO PODE PEGAR MAIS DE 3 LIVROS EMPRESTADOS';
    END IF;
END