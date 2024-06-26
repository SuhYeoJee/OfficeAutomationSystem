ALTER TABLE `nova_db`.`powder` 
ADD COLUMN `sys_reg_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성' AFTER `sys_id`,
ADD COLUMN `sys_update_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '자동생성' AFTER `sys_reg_date`,
ADD COLUMN `sys_description` VARCHAR(300) NULL DEFAULT NULL AFTER `sys_update_date`,
ADD UNIQUE INDEX `sys_id_UNIQUE` (`sys_id` ASC) VISIBLE;
;
