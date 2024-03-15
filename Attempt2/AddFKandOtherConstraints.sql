ALTER TABLE [PRACTICE2].[Portfolios]
ADD CONSTRAINT [fk_portfolios_clients] FOREIGN KEY ([Client_ID]) 
REFERENCES [PRACTICE2].[Clients] ([Client_ID]);

ALTER TABLE [PRACTICE2].[Positions]
ADD CONSTRAINT [fk_positions_portfolios] FOREIGN KEY ([Portfolio_ID]) 
REFERENCES [PRACTICE2].[Portfolios] ([Portfolio_ID]);

ALTER TABLE [PRACTICE2].[Positions]
ADD CONSTRAINT [fk_positions_assets] FOREIGN KEY ([Asset_ID]) 
REFERENCES [PRACTICE2].[Assets] ([AssetID]);

ALTER TABLE [PRACTICE2].[Prices]
ADD CONSTRAINT [fk_prices_assets] FOREIGN KEY ([Asset_ID]) 
REFERENCES [PRACTICE2].[Assets] ([AssetID]);

ALTER TABLE [PRACTICE2].[Assets]
ADD CONSTRAINT [chk_asset_type] CHECK ([Asset_Type] IN ('Equity', 'Bond', 'Commodity', 'Currency', 'Mutual Fund', 'ETF', 'Option', 'Future','Cryptocurrency'));