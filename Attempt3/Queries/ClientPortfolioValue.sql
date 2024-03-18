--Clients Portfolio Value On a given Day
SELECT 
    p.Client_ID,
    p.Portfolio_ID,
    p.Portfolio_Name,
    SUM(pos.Quantity * pr.Price_Close) AS Portfolio_Value
FROM 
    [PRACTICE3].[Clients] c
JOIN 
    [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
JOIN 
    [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
JOIN 
    [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol AND pr.Date = '2023-12-19'
WHERE 
    c.Client_Name = 'Alex Johnson'
GROUP BY 
    p.Client_ID,
    p.Portfolio_ID,
    p.Portfolio_Name;

--Client Portfolio values over certain days (Showing the returns)
WITH PortfolioValues AS (
    SELECT 
        p.Portfolio_ID,
        pr.Date,
        SUM(pos.Quantity * pr.Price_Close) AS TotalValue
    FROM 
        [PRACTICE3].[Clients] c
    JOIN 
        [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
    JOIN 
        [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN 
        [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol
    WHERE 
        c.Client_Name = 'Alex Johnson'
        AND pr.Date BETWEEN '2023-02-01' AND '2023-02-28'
    GROUP BY 
        p.Portfolio_ID,
        pr.Date
),
DailyReturns AS (
    SELECT 
        Portfolio_ID,
        Date,
        TotalValue,
        -- Calculate the daily return
        (TotalValue - LAG(TotalValue, 1) OVER (PARTITION BY Portfolio_ID ORDER BY Date)) / LAG(TotalValue, 1) OVER (PARTITION BY Portfolio_ID ORDER BY Date) AS DailyReturn
    FROM 
        PortfolioValues
)
SELECT * 
FROM DailyReturns
WHERE DailyReturn IS NOT NULL -- Exclude the first day as it has no previous day's value to compare
ORDER BY 
    Portfolio_ID,
    Date;
