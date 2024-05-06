CREATE DEFINER=`root`@`localhost` TRIGGER `bond_BEFORE_INSERT` BEFORE INSERT ON `bond` FOR EACH ROW BEGIN
    DECLARE powder_price_decimal DECIMAL(10, 2);

    IF NEW.Co IS NOT NULL THEN
        SET powder_price_decimal = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'C') AS DECIMAL(10, 2));
		SET NEW.Fe = (SELECT price FROM powder WHERE powder.chemical_symbol = 'C');
        SET NEW.price = CAST(CAST(NEW.Co AS DECIMAL(10, 2)) * powder_price_decimal AS DECIMAL(10, 2));
    END IF;
END