CREATE DEFINER = CURRENT_USER TRIGGER `db_academico`.`tb_notas_BEFORE_INSERT_1` BEFORE INSERT ON `tb_notas` FOR EACH ROW
FOR EACH ROW
BEGIN
    IF NEW.nota > 10 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A nota não pode ser maior que 10';
    END IF;

    IF NEW.nota < 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A nota não pode ser menor que 0';
    END IF;
END