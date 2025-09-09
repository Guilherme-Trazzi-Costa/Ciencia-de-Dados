CREATE DEFINER = CURRENT_USER TRIGGER `db_academico`.`tb_matriculas_BEFORE_INSERT` BEFORE INSERT ON `tb_matriculas` FOR EACH ROW
BEGIN
    SET NEW.data_matricula = CURDATE();
    -- se quiser também horário, use NOW() em vez de CURDATE()
END
