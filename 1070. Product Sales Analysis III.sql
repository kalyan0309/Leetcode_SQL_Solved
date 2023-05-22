/* Write your T-SQL query statement below */
WITH CTE AS 
(
    SELECT product_id,MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)
SELECT c.product_id,first_year,quantity,price
FROM CTE AS c
INNER JOIN Sales s
ON c.product_id = s.product_id AND c.first_year = s.year
