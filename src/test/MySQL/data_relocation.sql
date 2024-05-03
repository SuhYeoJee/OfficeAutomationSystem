use nova_db;

INSERT INTO nova_db.powder (chemical_symbol, name_en, name_ko, spec, density, price, inventory)
SELECT chemical_symbol, name_en, name_ko, spec, density, price, inventory FROM nova.powder;

SELECT DISTINCT * FROM `powder` ; 