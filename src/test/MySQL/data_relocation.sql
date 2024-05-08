use nova_db;

INSERT INTO nova_db.shank (
product_name,price,specification
)
SELECT 
product_name,price,specification
FROM nova.shank;

SELECT DISTINCT * FROM nova_db.shank ; 