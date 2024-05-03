-- TRUNCATE TABLE bond;
use nova_db;
CREATE TABLE powder (
    sys_id VARCHAR(11) PRIMARY KEY
);

DELIMITER //

CREATE TRIGGER before_powder_insert
BEFORE INSERT ON powder
FOR EACH ROW
BEGIN
    DECLARE next_id INT;

    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM powder;
    
    SET NEW.sys_id = CONCAT('PO', LPAD(next_id, 9, '0'));
END//

DELIMITER ;
