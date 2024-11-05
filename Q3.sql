SELECT 
    Year,
    Quarter,
    COUNT(DISTINCT `Client Key`) AS Unique_Clients
FROM (
    -- Product 1 go-live dates
    SELECT 
        `Client Key`,
        YEAR(STR_TO_DATE(`Product 1 Go Live Date`, '%m/%d/%Y')) AS Year,
        QUARTER(STR_TO_DATE(`Product 1 Go Live Date`, '%m/%d/%Y')) AS Quarter
    FROM Progyny_MetaData_1
    WHERE `Product 1 Go Live Date` IS NOT NULL

    UNION

    -- Product 2 go-live dates
    SELECT 
        `Client Key`,
        YEAR(STR_TO_DATE(`Product 2 Go Live Date`, '%m/%d/%Y')) AS Year,
        QUARTER(STR_TO_DATE(`Product 2 Go Live Date`, '%m/%d/%Y')) AS Quarter
    FROM Progyny_MetaData_1
    WHERE `Product 2 Go Live Date` IS NOT NULL
) AS combined_go_live_dates
GROUP BY Year, Quarter
ORDER BY Year, Quarter;
