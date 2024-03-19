CREATE OR ALTER VIEW [PRACTICE3].[PortfolioHistoricalPerformanceView] AS
SELECT
    p.Portfolio_ID,
    pr.Date,
    SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pr.Price_Close ELSE 0 END) AS PortfolioValue,
    ISNULL(SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pos.PurchasePrice END), 0) AS CapitalInvested,
    CASE 
        WHEN ISNULL(SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pos.PurchasePrice END), 0) > 0 
        THEN (SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pr.Price_Close ELSE 0 END) - ISNULL(SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pos.PurchasePrice END), 0)) 
             / NULLIF(ISNULL(SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pos.PurchasePrice END), 0), 0) 
        ELSE NULL 
    END AS ROI
FROM
    [PRACTICE3].[Portfolios] p
JOIN
    [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
JOIN
    [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol
GROUP BY
    p.Portfolio_ID, pr.Date;
