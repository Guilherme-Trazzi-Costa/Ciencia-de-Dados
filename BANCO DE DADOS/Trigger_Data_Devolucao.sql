CREATE DEFINER = CURRENT_USER TRIGGER `db_biblioteca`.`Data_devolucao` BEFORE INSERT ON `tb_emprestimos` FOR EACH ROW
BEGIN
	SET NEW.data_devolucao = DATE_ADD(New.data_emprestimos, INTERVAL 15 DAY);
END
