use nova_db;

INSERT INTO nova_db.item (
`name`,group_name,seg1_no,seg1_amount,seg2_no,seg2_amount,shank_no,shank_amount,sub1_no,sub1_amount,sub2_no,sub2_amount,mark
)
SELECT 
`name`,groupName,seg1No,seg1Amount,seg2No,seg2Amount,shank,shankAmount,sub1No,sub2No,sub2Amount,color,mark
FROM nova.product;

SELECT DISTINCT * FROM nova_db.item ; 