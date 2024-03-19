CREATE TRIGGER SetPurchasePrice
ON [CW1].[Positions]
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE p
    SET p.PurchasePrice = pr.Price_Close
    FROM [CW1].[Positions] p
    INNER JOIN inserted i ON p.Position_ID = i.Position_ID
    INNER JOIN [CW1].[Prices] pr ON i.Asset_Symbol = pr.Asset_Symbol AND i.PurchaseDate = pr.Date
END;
GO

CREATE TRIGGER UpdateCurrentPrice
ON [CW1].[Positions]
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE p
    SET p.CurrentPrice = pr.Price_Close
    FROM [CW1].[Positions] p
    INNER JOIN inserted i ON p.Position_ID = i.Position_ID
    CROSS APPLY (
        SELECT TOP 1 Price_Close
        FROM [CW1].[Prices] pr
        WHERE pr.Asset_Symbol = i.Asset_Symbol
        ORDER BY pr.Date DESC
    ) pr
END;
GO