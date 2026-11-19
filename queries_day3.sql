--Aggregate queries 

-- Querie using COUNT
SELECT COUNT(*)
FROM sales_data_sample;

--Querie using SUM
SELECT SUM(c5) AS total_sales
FROM sales_data_sample;

--Querie using AVG
SELECT AVG(c5) AS average_sales
from sales_data_sample;

--Querie using MAX 
SELECT MAX(CAST(c5 AS DECIMAL(10,2))) AS maximum_sales
FROM sales_data_sample;

--Querie using MIN 
SELECT MIN(c5) AS minimum_sales
FROM sales_data_sample;

--Queries using SUM with GROUP BY 
SELECT c2, SUM(c5) AS total_sales
FROM sales_data_sample
GROUP BY c2;

--Query using AVG with GROUP BY
SELECT c3, AVG(c5) AS average_sales
FROM sales_data_sample
GROUP BY c3;

--Query using COUNT DISTINCT
SELECT COUNT(DISTINCT c1) AS unique_customers
FROM sales_data_sample;

-- GROUP BY region 
SELECT c22 AS Region, 
       SUM(CAST(c5 as REAL)) as total_sales
FROM sales_data_sample
GROUP BY Region;

--GROUP BY Category
SELECT c11 as Category,
       SUM(CAST(c5 as REAL)) as total_sales
FROM sales_data_sample
GROUP BY Category;

--GROUP BY Month 
SELECT c9 as Month,
       SUM(CAST(c5 as REAL)) as total_sales
FROM sales_data_sample
GROUP BY Month
ORDER BY Month;

-- Filter aggregated results using HAVING
SELECT
    c11 as Category,
    SUM(CAST(c5 AS REAL)) AS total_sales
FROM sales_data_sample
GROUP BY Category
HAVING SUM(CAST(c5 AS REAL)) > 100000;

-- Window Function using SUM() OVER()
SELECT
    c1 as Order_Number,
    CAST(c5 AS REAL) AS sales,
    SUM(CAST(c5 AS REAL)) OVER() AS overall_sales
FROM sales_data_sample;