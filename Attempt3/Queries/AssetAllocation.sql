SELECT
    p.Portfolio_ID,
    p.Portfolio_Name,
    pr.Date,
    a.Asset_Type,
    SUM(pos.Quantity * pr.Price_Close) AS Asset_Type_Value,
    pt.Total_Portfolio_Value,
    (SUM(pos.Quantity * pr.Price_Close) / pt.Total_Portfolio_Value) * 100 AS Asset_Type_Percentage
FROM
    [PRACTICE3].[Clients] c
JOIN
    [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
JOIN
    [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
JOIN
    [PRACTICE3].[Assets] a ON pos.Asset_Symbol = a.AssetSymbol
JOIN
    [PRACTICE3].[Prices] pr ON a.AssetSymbol = pr.Asset_Symbol
CROSS APPLY (
    SELECT
        SUM(posInner.Quantity * prInner.Price_Close) AS Total_Portfolio_Value
    FROM
        [PRACTICE3].[Positions] posInner
    JOIN
        [PRACTICE3].[Prices] prInner ON posInner.Asset_Symbol = prInner.Asset_Symbol
    WHERE
        posInner.Portfolio_ID = p.Portfolio_ID AND prInner.Date = pr.Date
) pt
WHERE
    c.Client_Name = 'Maria Garcia'
GROUP BY
    p.Portfolio_ID,
    p.Portfolio_Name,
    pr.Date,
    a.Asset_Type,
    pt.Total_Portfolio_Value
ORDER BY
    p.Portfolio_ID,
    pr.Date,
    a.Asset_Type;