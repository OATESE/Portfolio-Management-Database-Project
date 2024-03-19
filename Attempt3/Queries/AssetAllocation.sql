WITH PortfolioValues AS (
    SELECT
        p.Portfolio_ID,
        pr.Date,
        a.Asset_Type,
        pos.Quantity * pr.Price_Close AS AssetTypeValue
    FROM
        [PRACTICE3].[Clients] c
    JOIN [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
    JOIN [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN [PRACTICE3].[Assets] a ON pos.Asset_Symbol = a.AssetSymbol
    JOIN [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol AND pos.PurchaseDate <= pr.Date
    WHERE
        c.Client_Name = 'Alex Johnson'
),
PortfolioTotalValues AS (
    SELECT
        Portfolio_ID,
        Date,
        SUM(AssetTypeValue) AS TotalValue
    FROM PortfolioValues
    GROUP BY Portfolio_ID, Date
)
SELECT
    pvt.Portfolio_ID,
    pvt.Date,
    ISNULL([Equity] / ptv.TotalValue, 0) AS StockProportion,
    ISNULL([Bond] / ptv.TotalValue, 0) AS BondProportion,
    ISNULL([Commodity] / ptv.TotalValue, 0) AS CommodityProportion,
    ISNULL([Currency] / ptv.TotalValue, 0) AS CurrencyProportion,
    ISNULL([ETF] / ptv.TotalValue, 0) AS ETFProportion,
    ISNULL([MutualFund] / ptv.TotalValue, 0) AS MFProportion,
    ISNULL([Option] / ptv.TotalValue, 0) AS OptionProportion,
    ISNULL([Future] / ptv.TotalValue, 0) AS FutureProportion,
    ISNULL([Cryptocurrency] / ptv.TotalValue, 0) AS CryptoProportion
FROM
    PortfolioValues pv
PIVOT (
    SUM(AssetTypeValue)
    FOR Asset_Type IN ([Equity], [Bond], [Commodity], [Currency], [ETF], [MutualFund], [Option], [Future], [Cryptocurrency])
) AS pvt
JOIN PortfolioTotalValues ptv ON pvt.Portfolio_ID = ptv.Portfolio_ID AND pvt.Date = ptv.Date
ORDER BY
    pvt.Portfolio_ID, pvt.Date;
