CREATE TRIGGER SetPurchasePrice
ON [PRACTICE3].[Positions]
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE p
    SET p.PurchasePrice = pr.Price_Close
    FROM [PRACTICE3].[Positions] p
    INNER JOIN inserted i ON p.Position_ID = i.Position_ID
    INNER JOIN [PRACTICE3].[Prices] pr ON i.Asset_Symbol = pr.Asset_Symbol AND i.PurchaseDate = pr.Date
END;
GO