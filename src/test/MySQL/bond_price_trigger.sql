CREATE DEFINER=`root`@`localhost` TRIGGER `before_bond_insert` BEFORE INSERT ON `bond` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    DECLARE powder_ratio DECIMAL(10, 2);
    DECLARE powder_price DECIMAL(10, 2);
    DECLARE temp_ratio DECIMAL(10, 2);
    DECLARE temp_price DECIMAL(10, 2);
    -- ----------------------------------------------------------------------
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM bond;
    SET NEW.sys_id = CONCAT('BO', LPAD(next_id, 9, '0'));
    -- ----------------------------------------------------------------------
    SET powder_ratio = 0;
	SET powder_price = 0;

    IF NEW.C IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'C') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;
  
	IF NEW.Fe IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Fe') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;
    
	IF NEW.`Cu #300` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Cu #300') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Cu #600` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Cu #600') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Ni` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Ni') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`CuSn #67` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'CuSn #67') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`CuSn #80` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'CuSn #80') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;        
    
	IF NEW.`Sn #300` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Sn #300') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Sn #600` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Sn #600') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`W` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'W') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`WC` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'WC') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;         
    
	IF NEW.`W₂C` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'W₂C') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;        
    
	IF NEW.`S` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'S') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Ag` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Ag') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`P₂O₅` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'P₂O₅') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Zn` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Zn') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.C AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;         
    
	SET NEW.price = CAST(powder_price AS DECIMAL(10, 2));    
    -- ----------------------------------------------------------------------
END