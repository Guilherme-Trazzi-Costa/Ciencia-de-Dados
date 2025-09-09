CREATE DEFINER = CURRENT_USER TRIGGER `db_academico`.`tb_disciplinas_BEFORE_DELETE` BEFORE DELETE ON `tb_disciplinas` FOR EACH ROW
BEGIN
	    DECLARE qtd INT;

    -- Conta quantas matrículas existem para a disciplina que está sendo apagada
    SELECT COUNT(*) INTO qtd
    FROM tb_matriculas
    WHERE id_disciplina = OLD.id_disciplina;

    -- Se houver pelo menos 1, impede exclusão
    IF qtd > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Não é permitido excluir disciplina com estudantes matriculados';
    END IF;
END
