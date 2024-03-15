CREATE TABLE [PRACTICE].[Clients] (
    [Client_ID] INT NOT NULL,
    [Client_Name] VARCHAR(255) NOT NULL,
    [Client_Address] VARCHAR(255),
    [Client_Number] VARCHAR(50),
    CONSTRAINT [pk_Clients] PRIMARY KEY ([Client_ID])
);

CREATE TABLE [PRACTICE].[Portfolios] (
    [Portfolio_ID] INT NOT NULL,
    [Client_ID] INT NOT NULL,
    [Portfolio_Name] VARCHAR(255) NOT NULL,
    [Portfolio_Description] VARCHAR(500),
    [Portfolio_Purpose] VARCHAR(255),
    [Portfolio_Init_Date] DATE NOT NULL,
    CONSTRAINT [pk_Portfolios] PRIMARY KEY ([Portfolio_ID])
);

CREATE TABLE [PRACTICE].[Assets] (
    [AssetID] INT NOT NULL,
    [AssetType] VARCHAR(50) NOT NULL,
    [Symbol] VARCHAR(10) NOT NULL,
    [Industry] VARCHAR(100),
    [Income_providing] BIT,
    CONSTRAINT [pk_Assets] PRIMARY KEY ([AssetID])
);

CREATE TABLE [PRACTICE].[Positions] (
    [Position_ID] INT NOT NULL,
    [Portfolio_ID] INT NOT NULL,
    [Asset_ID] INT NOT NULL,
    [Quantity] DECIMAL(19,4) NOT NULL,
    [PurchaseDate] DATE NOT NULL,
    [PurchasePrice] DECIMAL(19,4) NOT NULL,
    [CurrentPrice] DECIMAL(19,4) NOT NULL,
    CONSTRAINT [pk_Positions] PRIMARY KEY ([Position_ID])
);

CREATE TABLE [PRACTICE].[Prices] (
    [PriceID] INT NOT NULL,
    [Asset_ID] INT NOT NULL,
    [Date] DATE NOT NULL,
    [Price_Open] DECIMAL(19,4) NOT NULL,
    [Price_Close] DECIMAL(19,4) NOT NULL,
    [Price_High] DECIMAL(19,4) NOT NULL,
    [Price_Low] DECIMAL(19,4) NOT NULL,
    [Volume] BIGINT,
    CONSTRAINT [pk_Prices] PRIMARY KEY ([PriceID])
);
