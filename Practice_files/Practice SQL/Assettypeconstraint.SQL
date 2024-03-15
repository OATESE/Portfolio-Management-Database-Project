ALTER TABLE [PRACTICE].[Assets]
    ADD CONSTRAINT [chk_asset_type] CHECK ([AssetType] IN ('Equity', 'Bond', 'Commodity', 'Currency', 'Mutual Fund', 'ETF', 'Option', 'Future'));