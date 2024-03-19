-- Drop foreign key constraints in other tables that reference Assets.AssetID
ALTER TABLE [PRACTICE2].[Positions]
DROP CONSTRAINT [fk_positions_assets];

ALTER TABLE [PRACTICE2].[Prices]
DROP CONSTRAINT [fk_prices_assets];

-- Drop the current primary key constraint in the Assets table
-- You will need to know the name of the primary key constraint.
-- If you don't know it, you can find it using the SQL Server Management Studio or a similar tool.
ALTER TABLE [PRACTICE2].[Assets]
DROP CONSTRAINT [pk_assets];

-- Change the Symbol column to be the new primary key
ALTER TABLE [PRACTICE2].[Assets]
ADD CONSTRAINT [pk_assets_symbol] PRIMARY KEY ([Symbol]);

-- Update the foreign key constraints in other tables to reference Assets.Symbol
ALTER TABLE [PRACTICE2].[Positions]
ADD CONSTRAINT [fk_positions_assets] FOREIGN KEY ([Asset_Symbol]) -- Use the actual column name
REFERENCES [PRACTICE2].[Assets] ([Symbol]);

ALTER TABLE [PRACTICE2].[Prices]
ADD CONSTRAINT [fk_prices_assets] FOREIGN KEY ([Asset_Symbol]) -- Use the actual column name
REFERENCES [PRACTICE2].[Assets] ([Symbol]);