-- Calculate revenue breakdown for new vs. returning clients by year and type
WITH Client_First_Year AS (
    -- Step 1: Determine the first year of revenue for each client and type
    SELECT 
        `Client Key`,
        `Type`,
        MIN(YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y'))) AS First_Year
    FROM Data_Progyny_1
    GROUP BY `Client Key`, `Type`
),
Revenue_Breakdown AS (
    -- Step 2: Categorize revenue as new or returning for each client, year, and type
    SELECT 
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        d.`Type`,
        CASE 
            WHEN YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) = cf.First_Year THEN 'New Sales'
            ELSE 'Organic Growth'
        END AS Revenue_Type,
        CAST(REPLACE(d.`Rev`, ',', '') AS DECIMAL(15, 2)) AS Revenue
    FROM Data_Progyny_1 AS d
    JOIN Client_First_Year AS cf
    ON d.`Client Key` = cf.`Client Key` AND d.`Type` = cf.`Type`
    WHERE d.`Rev` IS NOT NULL
)
-- Step 3: Aggregate revenue by year, type, and revenue type
SELECT 
    Year,
    Type,
    Revenue_Type,
    SUM(Revenue) AS Total_Revenue
FROM Revenue_Breakdown
GROUP BY Year, Type, Revenue_Type
ORDER BY Type, Year, Revenue_Type;
