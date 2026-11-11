--Display all records
SELECT * 
from  sales_data_sample;

--Select specific column
SELECT c1,c2,c3
from sales_data_sample;

--Find order where sales greater than 3000
SELECT c1,c23,c24,c5
from sales_data_sample
WHERE c5>3000;

--Find sales with quantiy above 30 and sales above 3000
SELECT c1,c23,c24,c5,c2
FROM sales_data_sample
where c5>3000 AND c2>30;

--Find sales with quantity above 50 or sales above 5000
SELECT c1,c23,c24,c5,c2
FROM sales_data_sample
where c5>5000 OR c2>50;

--Exclude cancelled orders
SELECT *
from sales_data_sample
where NOT c7='cancelled';

--Customers whose name starts with A
select c1,c23,c24
from sales_data_sample
where c24 like 'A%';

--Orders from selected countires
select c1,c23,c24,c21
from sales_data_sample
where c21 in ('USA','France');

--sales between 1000 and 3000
SELECT c1,c23,c24,c5,c2
FROM sales_data_sample
where c5 BETWEEN 1000 and 3000;

--Records with missing state information
SELECT c1,c23,c24,c5,c19
from sales_data_sample
where c19 ISNULL;