CREATE OR ALTER PROCEDURE WeekendPrices
AS
BEGIN
    -- Temporary table to hold distinct dates
    DECLARE @DateList TABLE (PriceDate DATE);
    
    -- Populate @DateList with all distinct dates from Prices table
    INSERT INTO @DateList (PriceDate)
    SELECT DISTINCT Date FROM [CW1].[Prices] ORDER BY Date;

    -- Temporary table to hold distinct assets
    DECLARE @AssetList TABLE (AssetSymbol VARCHAR(255));
    
    -- Populate @AssetList with all distinct assets
    INSERT INTO @AssetList (AssetSymbol)
    SELECT DISTINCT Asset_Symbol FROM [CW1].[Prices];

    -- Cursor to iterate over each asset
    DECLARE AssetCursor CURSOR FOR
    SELECT AssetSymbol FROM @AssetList;
    DECLARE @CurrentAsset VARCHAR(255);

    OPEN AssetCursor;
    FETCH NEXT FROM AssetCursor INTO @CurrentAsset;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Cursor to iterate over each date
        DECLARE DateCursor CURSOR FOR
        SELECT PriceDate FROM @DateList;
        DECLARE @CurrentDate DATE;

        OPEN DateCursor;
        FETCH NEXT FROM DateCursor INTO @CurrentDate;

        WHILE @@FETCH_STATUS = 0
        BEGIN
            -- Check if price exists for the current asset on the current date
            IF NOT EXISTS (SELECT 1 FROM [CW1].[Prices] WHERE Asset_Symbol = @CurrentAsset AND Date = @CurrentDate)
            BEGIN
                -- Find the most recent price before @CurrentDate for @CurrentAsset
                DECLARE @MostRecentPrice DECIMAL(19, 4);
                SELECT TOP 1 @MostRecentPrice = Price_Close
                FROM [CW1].[Prices]
                WHERE Asset_Symbol = @CurrentAsset AND Date < @CurrentDate
                ORDER BY Date DESC;

                -- Insert the most recent price for the missing date, replicating for Open, High, Low, and using a default for Volume if necessary
                IF @MostRecentPrice IS NOT NULL
                BEGIN
                    INSERT INTO [CW1].[Prices] 
                    (Asset_Symbol, Date, Price_Open, Price_High, Price_Low, Price_Close, Volume)
                    VALUES 
                    (@CurrentAsset, @CurrentDate, @MostRecentPrice, @MostRecentPrice, @MostRecentPrice, @MostRecentPrice, 0); -- Assuming '0' as a default value for Volume
                END
            END

            FETCH NEXT FROM DateCursor INTO @CurrentDate;
        END

        CLOSE DateCursor;
        DEALLOCATE DateCursor;

        FETCH NEXT FROM AssetCursor INTO @CurrentAsset;
    END

    CLOSE AssetCursor;
    DEALLOCATE AssetCursor;
END