/*
This kata is inspired by SQL Basics: Simple PIVOTING data by matt c.

You need to build a pivot table WITHOUT using CROSSTAB function. Having two tables products and details you need to select a pivot table of products with counts of details occurrences (possible details values are ['good', 'ok', 'bad'].

Results should be ordered by product's name.

Model schema for the kata is:

product:    details:
id          id
name        product_id
            detail
product: id ---> details: product_id

your query should return table with next columns

name
good
ok
bad
*/

SELECT name, good, ok, bad
FROM products p
INNER JOIN (SELECT t1.product_id, good, ok, bad
FROM (select product_id, count(detail) as good from details where detail = 'good' group by product_id) as t1
INNER JOIN (select product_id, count(detail) as ok from details where detail = 'ok' group by product_id) as t2
ON t1.product_id = t2.product_id
INNER JOIN (select product_id, count(detail) as bad from details where detail = 'bad' group by product_id) as t3
ON t1.product_id = t3.product_id) as d
ON p.id = d.product_id
ORDER BY name
