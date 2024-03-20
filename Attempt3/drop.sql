SELECT phpv.Portfolio_ID, phpv.Date, phpv.PortfolioValue, phpv.CapitalInvested, phpv.ROI
FROM [CW1].[PortfolioHistoricalPerformanceView] phpv
JOIN [CW1].[Portfolios] p ON phpv.Portfolio_ID = p.Portfolio_ID
JOIN [CW1].[Clients] c ON p.Client_ID = c.Client_ID
WHERE c.Client_Name = 'Alex Johnson'
ORDER BY phpv.Portfolio_ID, phpv.Date;
