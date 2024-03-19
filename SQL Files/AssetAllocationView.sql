--Asset Allocation View
CREATE OR ALTER VIEW [CW1].[AssetAllocationView2] AS
WITH PortfolioAssetValues AS (
    SELECT
        p.Portfolio_ID,
        pr.Date,
        a.Asset_Type,
        SUM(pos.Quantity * pr.Price_Close) AS Value
    FROM
        [CW1].[Portfolios] p
    JOIN [CW1].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN [CW1].[Assets] a ON pos.Asset_Symbol = a.AssetSymbol
    JOIN [CW1].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol
    GROUP BY p.Portfolio_ID, pr.Date, a.Asset_Type
),
PortfolioTotalValues AS (
    SELECT
        Portfolio_ID,
        Date,
        SUM(Value) AS TotalValue
    FROM PortfolioAssetValues
    GROUP BY Portfolio_ID, Date
)
SELECT
    p.Portfolio_ID,
    p.Date,
    ISNULL(p.[Equity] / t.TotalValue, 0) AS 'EquityProportion',
    ISNULL(p.[Bond] / t.TotalValue, 0) AS 'BondProportion',
    ISNULL(p.[Commodity] / t.TotalValue, 0) AS 'CommodityProportion',
    ISNULL(p.[Currency] / t.TotalValue, 0) AS 'CurrencyProportion',
    ISNULL(p.[ETF] / t.TotalValue, 0) AS 'ETFProportion',
    ISNULL(p.[MutualFund] / t.TotalValue, 0) AS 'MutualFundProportion',
    ISNULL(p.[Option] / t.TotalValue, 0) AS 'OptionProportion',
    ISNULL(p.[Future] / t.TotalValue, 0) AS 'FutureProportion',
    ISNULL(p.[Cryptocurrency] / t.TotalValue, 0) AS 'CryptocurrencyProportion'
FROM
    PortfolioAssetValues
PIVOT (
    SUM(Value)
    FOR Asset_Type IN ([Equity], [Bond], [Commodity], [Currency], [ETF], [MutualFund], [Option], [Future], [Cryptocurrency])
) AS p
JOIN PortfolioTotalValues t ON p.Portfolio_ID = t.Portfolio_ID AND p.Date = t.Date
