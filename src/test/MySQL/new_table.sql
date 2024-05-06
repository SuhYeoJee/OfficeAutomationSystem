USE nova_db;

-- 테이블 생성 및 수정
CREATE TABLE IF NOT EXISTS bond (
    sys_id VARCHAR(11) PRIMARY KEY,
    sys_reg_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
    sys_update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '자동생성',
    sys_description VARCHAR(300) NULL DEFAULT NULL,
    UNIQUE INDEX sys_id_UNIQUE (sys_id ASC)
);

DELIMITER //

-- sys_id 생성 트리거
CREATE TRIGGER before_bond_insert
BEFORE INSERT ON bond
FOR EACH ROW
BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM bond;
    SET NEW.sys_id = CONCAT('BO', LPAD(next_id, 9, '0'));
END//

DELIMITER ;
