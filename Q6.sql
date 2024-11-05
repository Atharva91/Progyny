-- Calculate the percentage of clients with Product 2 by year
WITH Yearly_Client_Count AS (
    -- Step 1: Count total unique clients per year
    SELECT 
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        COUNT(DISTINCT `Client Key`) AS Total_Clients
    FROM Data_Progyny_1
    WHERE `DOS` IS NOT NULL
    GROUP BY Year
),
Yearly_Product2_Client_Count AS (
    -- Step 2: Count unique clients with Product 2 per year
    SELECT 
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        COUNT(DISTINCT `Client Key`) AS Product_2_Clients
    FROM Data_Progyny_1
    WHERE `DOS` IS NOT NULL AND `Type` = 'Product 2'
    GROUP BY Year
)
-- Step 3: Calculate the percentage of clients with Product 2 per year
SELECT 
    yc.Year,
    yc.Total_Clients,
    p2c.Product_2_Clients,
    (p2c.Product_2_Clients / yc.Total_Clients) * 100 AS Product_2_Percentage
FROM Yearly_Client_Count AS yc
JOIN Yearly_Product2_Client_Count AS p2c
ON yc.Year = p2c.Year
ORDER BY yc.Year;
