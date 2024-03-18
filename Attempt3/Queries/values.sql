SELECT
    p.Portfolio_ID,
    p.Portfolio_Name,
    pr.Date,
    SUM(pos.Quantity * pr.Price_Close) AS Portfolio_Value,
    SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pos.PurchasePrice ELSE 0 END) AS Amount_Invested_Up_To_Date
FROM
    [PRACTICE3].[Clients] c
JOIN
    [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
JOIN
    [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
JOIN
    [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol AND pos.PurchaseDate <= pr.Date
WHERE
    c.Client_Name = 'Alex Johnson'
GROUP BY
    p.Portfolio_ID, p.Portfolio_Name, pr.Date
ORDER BY
    p.Portfolio_ID, pr.Date;