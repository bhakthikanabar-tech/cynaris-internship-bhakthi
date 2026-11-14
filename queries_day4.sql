-- Non-correlated subquery – Find above-average sales
SELECT * 
FROM sales_data_sample
WHERE c5>(
  SELECT AVG(c5)
  FROM sales_data_sample)
 ORDER BY c5;
 
 --Correlated subquery – Find the top performer per region
 SELECT *
 FROM sales_data_sample s1
 WHERE c5 = (
   SELECT MAX(s2.c5)
   from sales_data_sample s2
   where s2.c22= s1.c22
   );
   
 --Rewrite a nested subquery as a CTE
 WITH AverageSales AS (
    SELECT AVG(c5) AS avg_sales
    FROM sales_data_sample
)
SELECT *
FROM sales_data_sample
WHERE c5 > (
    SELECT avg_sales
    FROM AverageSales
);

-- Chain two CTEs in a single query
WITH TerritorySales AS (
    SELECT
        c22,
        SUM(c5) AS total_sales
    FROM sales_data_sample
    GROUP BY c22
),
AverageTerritorySales AS (
    SELECT AVG(total_sales) AS avg_sales
    FROM TerritorySales
)
SELECT *
FROM TerritorySales
WHERE total_sales > (
    SELECT avg_sales
    FROM AverageTerritorySales
);