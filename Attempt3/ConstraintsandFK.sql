-- Foreign key constraint for Portfolios referencing Clients
ALTER TABLE [PRACTICE3].[Portfolios]
ADD CONSTRAINT [fk_portfolios_clients] FOREIGN KEY ([Client_ID]) 
REFERENCES [PRACTICE3].[Clients] ([Client_ID]);

-- Foreign key constraint for Positions referencing Portfolios
ALTER TABLE [PRACTICE3].[Positions]
ADD CONSTRAINT [fk_positions_portfolios] FOREIGN KEY ([Portfolio_ID]) 
REFERENCES [PRACTICE3].[Portfolios] ([Portfolio_ID]);

-- Foreign key constraint for Positions referencing Assets (using AssetSymbol)
ALTER TABLE [PRACTICE3].[Positions]
ADD CONSTRAINT [fk_positions_assets] FOREIGN KEY ([Asset_Symbol]) 
REFERENCES [PRACTICE3].[Assets] ([AssetSymbol]);

-- Foreign key constraint for Prices referencing Assets (using AssetSymbol)
ALTER TABLE [PRACTICE3].[Prices]
ADD CONSTRAINT [fk_prices_assets] FOREIGN KEY ([Asset_Symbol]) 
REFERENCES [PRACTICE3].[Assets] ([AssetSymbol]);

-- Check constraint for allowed Asset Types in Assets
ALTER TABLE [PRACTICE3].[Assets]
ADD CONSTRAINT [chk_asset_type] CHECK ([Asset_Type] IN ('Equity', 'Bond', 'Commodity', 'Currency', 'Mutual Fund', 'ETF', 'Option', 'Future','Cryptocurrency'));

-- Unique constraint for AssetSymbol in Assets
ALTER TABLE [PRACTICE3].[Assets]
ADD CONSTRAINT [uc_asset_symbol] UNIQUE ([AssetSymbol]);


ALTER TABLE [PRACTICE3].[Clients]
ADD CONSTRAINT [chk_client_email_format] CHECK (
    Client_Email LIKE '%@%.%' AND
    Client_Email NOT LIKE '%@%@%' AND
    Client_Email NOT LIKE '%..%' AND
    LEN(Client_Email) - LEN(REPLACE(Client_Email, '@', '')) = 1
);