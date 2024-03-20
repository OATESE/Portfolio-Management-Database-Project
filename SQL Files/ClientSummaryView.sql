--Client Summary Info View
CREATE OR ALTER VIEW [CW1].[ClientOverviewView] AS
WITH MostRecentDate AS (
    SELECT
        MAX(Date) AS RecentDate
    FROM
        [CW1].[PortfolioHistoricalPerformanceView]
), AggregatedClientData AS (
    SELECT
        c.Client_ID,
        c.Client_Name,
        SUM(ph.PortfolioValue) AS TotalAUM, -- Total Assets Under Management on the most recent date
        (SUM(ph.PortfolioValue) - SUM(ph.CapitalInvested)) / NULLIF(SUM(ph.CapitalInvested), 0) AS OverallROI, -- Overall Return on Investment
        COUNT(DISTINCT p.Portfolio_ID) AS NumberOfPortfolios,
        COUNT(DISTINCT a.Asset_Type) AS NumberOfAssetTypes
    FROM
        [CW1].[Clients] c
    JOIN
        [CW1].[Portfolios] p ON c.Client_ID = p.Client_ID
    JOIN
        [CW1].[PortfolioHistoricalPerformanceView] ph ON p.Portfolio_ID = ph.Portfolio_ID
    JOIN
        [CW1].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN
        [CW1].[Assets] a ON pos.Asset_Symbol = a.AssetSymbol
    WHERE
        ph.Date = (SELECT RecentDate FROM MostRecentDate)
    GROUP BY
        c.Client_ID, c.Client_Name
)
SELECT *
FROM
    AggregatedClientData


