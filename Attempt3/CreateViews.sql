CREATE VIEW [PRACTICE3].[AssetAllocationsView] AS
SELECT
    pv.Portfolio_ID,
    pv.Date,
    pv.Asset_Type,
    pv.AssetTypeValue,
    pv.AssetTypeValue / ptv.TotalValue AS Proportion
FROM
    (SELECT
        p.Portfolio_ID,
        pr.Date,
        a.Asset_Type,
        SUM(pos.Quantity * pr.Price_Close) AS AssetTypeValue
    FROM [PRACTICE3].[Portfolios] p
    JOIN [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN [PRACTICE3].[Assets] a ON pos.Asset_Symbol = a.AssetSymbol
    JOIN [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol
    GROUP BY p.Portfolio_ID, pr.Date, a.Asset_Type) AS pv
JOIN
    (SELECT
        Portfolio_ID,
        Date,
        SUM(Quantity * Price_Close) AS TotalValue
    FROM [PRACTICE3].[Positions] pos
    JOIN [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol
    GROUP BY Portfolio_ID, Date) AS ptv ON pv.Portfolio_ID = ptv.Portfolio_ID AND pv.Date = ptv.Date;
