CREATE DEFINER=`root`@`localhost` TRIGGER `tb_pets_BEFORE_INSERT` BEFORE INSERT ON `tb_pets` FOR EACH ROW BEGIN
	SET NEW.idade_pet = timestampdiff(YEAR, NEW.data_nascimento, curdate());
END