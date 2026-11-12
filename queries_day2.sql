--Creating 2 different tables for practice

--Customer Table
CREATE TABLE customers AS
SELECT DISTINCT
    c14 AS customer_name,
    c15 AS phone,
    c18 AS city,
    c19 AS state,
    c20 AS postal_code,
    c21 AS country
FROM sales_data_sample;


--Order table
CREATE TABLE orders AS
SELECT
    c1 AS order_number,
    c14 AS customer_name,
    c6 AS order_date,
    c7 AS status,
    c13 AS product_code,
    c11 AS product_line,
    c2 AS quantity_ordered,
    c3 AS price_each,
    c5 AS sales,
    c25 AS deal_size
FROM sales_data_sample;

-- Practicing JOIN quesries

--INNER JOIN
SELECT o.order_number, c.customer_name, o.order_date, o.status,c.phone
FROM customers as c
INNER JOIN orders as o 
on c.customer_name = o.customer_name
WHERE o.status='Shipped';

--LEFT JOIN
SELECT
    c.customer_name,
    o.order_number,
    c.city,
    c.phone
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_name = o.customer_name;

--RIGHT JOIN 
SELECT c.customer_name, o.order_number, o.status,o.sales
FROM customers AS c 
RIGHT JOIN orders AS o 
ON c.customer_name=o.customer_name;

--FULL JOIN
SELECT
    c.customer_name,
    c.city,
    o.order_number,
    o.sales,
    o.status
FROM customers AS c
FULL OUTER JOIN orders AS o
ON c.customer_name = o.customer_name;

--SELF JOIN 
SELECT
    o1.customer_name,
    o1.order_number AS first_order,
    o2.order_number AS second_order
FROM orders AS o1
INNER JOIN orders AS o2
ON o1.customer_name = o2.customer_name
AND o1.order_number < o2.order_number
LIMIT 20;