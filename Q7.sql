-- Calculate Product 2 revenue as a percentage of Product 1 revenue for clients who have Product 2
WITH Client_Product_Revenue AS (
    -- Step 1: Calculate total revenue per client for each product type
    SELECT 
        `Client Key`,
        `Type`,
        SUM(CAST(REPLACE(`Rev`, ',', '') AS DECIMAL(15, 2))) AS Total_Revenue
    FROM Data_Progyny_1
    WHERE `Rev` IS NOT NULL
    GROUP BY `Client Key`, `Type`
),
Clients_With_Product_2 AS (
    -- Step 2: Filter to include only clients who have Product 2
    SELECT DISTINCT `Client Key`
    FROM Client_Product_Revenue
    WHERE `Type` = 'Product 2'
)
-- Step 3: Calculate Product 2 revenue as a percentage of Product 1 revenue for clients with Product 2
SELECT 
    cwp.`Client Key`,
    COALESCE(p1.Total_Revenue, 0) AS Product_1_Revenue,
    p2.Total_Revenue AS Product_2_Revenue,
    CASE 
        WHEN COALESCE(p1.Total_Revenue, 0) > 0 THEN (p2.Total_Revenue / p1.Total_Revenue) * 100
        ELSE NULL
    END AS Product_2_As_Percent_of_Product_1
FROM Clients_With_Product_2 AS cwp
LEFT JOIN Client_Product_Revenue AS p1 ON cwp.`Client Key` = p1.`Client Key` AND p1.`Type` = 'Product 1'
JOIN Client_Product_Revenue AS p2 ON cwp.`Client Key` = p2.`Client Key` AND p2.`Type` = 'Product 2';
