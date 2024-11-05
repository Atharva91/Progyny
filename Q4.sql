-- Calculate the annual revenue and revenue growth for each product type
SELECT 
    Year,
    Type,
    SUM(Revenue) AS Annual_Revenue,
    LAG(SUM(Revenue)) OVER (PARTITION BY Type ORDER BY Year) AS Previous_Year_Revenue,
    (SUM(Revenue) - LAG(SUM(Revenue)) OVER (PARTITION BY Type ORDER BY Year)) / LAG(SUM(Revenue)) OVER (PARTITION BY Type ORDER BY Year) * 100 AS Revenue_Growth_Percentage
FROM (
    -- Extract year and revenue for each product type
    SELECT 
        `Client Key`,
        YEAR(STR_TO_DATE(`DOS`, '%m/%d/%Y')) AS Year,
        `Type`,
        CAST(REPLACE(`Rev`, ',', '') AS DECIMAL(15, 2)) AS Revenue
    FROM Data_Progyny_1
    WHERE `Rev` IS NOT NULL
) AS annual_revenue_data
GROUP BY Year, Type
ORDER BY Type, Year;
