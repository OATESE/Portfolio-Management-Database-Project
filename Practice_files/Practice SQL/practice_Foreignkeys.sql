ALTER TABLE [PRACTICE].[Portfolios]
    ADD CONSTRAINT [fk_Portfolios_Clients] FOREIGN KEY ([Client_ID]) 
        REFERENCES [PRACTICE].[Clients]([Client_ID]);

ALTER TABLE [PRACTICE].[Positions]
    ADD CONSTRAINT [fk_Positions_Portfolios] FOREIGN KEY ([Portfolio_ID]) 
        REFERENCES [PRACTICE].[Portfolios]([Portfolio_ID]);

ALTER TABLE [PRACTICE].[Positions]
    ADD CONSTRAINT [fk_Positions_Assets] FOREIGN KEY ([Asset_ID]) 
        REFERENCES [PRACTICE].[Assets]([AssetID]);

ALTER TABLE [PRACTICE].[Prices]
    ADD CONSTRAINT [fk_Prices_Assets] FOREIGN KEY ([Asset_ID]) 
        REFERENCES [PRACTICE].[Assets]([AssetID]);  