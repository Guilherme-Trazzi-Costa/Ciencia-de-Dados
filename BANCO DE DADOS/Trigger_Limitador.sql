CREATE DEFINER = `root`@`localhost` TRIGGER `Limitador de Emprestimos` BEFORE INSERT ON `tb_emprestimos` FOR EACH ROW
BEGIN
	DECLARE total_emprestimo INT;
    
    SELECT COUNT(*) INTO total_emprestimo FROM tb_emprestimos
    WHERE id_membro = NEW.id_membro AND data_devolucao > NOW();
    
-- Delimitador de emprestimos
	IF total_emprestimo >= 3 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'O membro não pode ter mais de 3 emprestimos ativos';
END IF;
END