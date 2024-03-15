CREATE TABLE [PRACTICE2].[Clients] (
    [Client_ID] INT IDENTITY(1,1) NOT NULL,
    [Client_Name] VARCHAR(255) NOT NULL,
    [Client_Address] VARCHAR(255),
    [Client_Number] VARCHAR(50),
    CONSTRAINT [pk_clients] PRIMARY KEY ([Client_ID])
);

CREATE TABLE [PRACTICE2].[Portfolios] (
    [Portfolio_ID] INT IDENTITY(1,1) NOT NULL,
    [Client_ID] INT NOT NULL,
    [Portfolio_Name] VARCHAR(255) NOT NULL,
    [Portfolio_Description] VARCHAR(500),
    [Portfolio_Purpose] VARCHAR(255),
    [Portfolio_Init_Date] DATE NOT NULL,
    CONSTRAINT [pk_portfolios] PRIMARY KEY ([Portfolio_ID])
);

CREATE TABLE [PRACTICE2].[Assets] (
    [AssetID] INT IDENTITY(1,1) NOT NULL,
    [Asset_Type] VARCHAR(50) NOT NULL,
    [Symbol] VARCHAR(10) NOT NULL,
    [Asset_Name] VARCHAR(100),
    [Industry] VARCHAR(100),
    [Income_providing] BIT,
    CONSTRAINT [pk_assets] PRIMARY KEY ([AssetID])
);

CREATE TABLE [PRACTICE2].[Positions] (
    [Position_ID] INT IDENTITY(1,1) NOT NULL,
    [Portfolio_ID] INT NOT NULL,
    [Asset_ID] INT NOT NULL,
    [Quantity] DECIMAL(19,4) NOT NULL,
    [PurchaseDate] DATE NOT NULL,
    [PurchasePrice] DECIMAL(19,4) NOT NULL,
    [CurrentPrice] DECIMAL(19,4) NOT NULL,
    CONSTRAINT [pk_positions] PRIMARY KEY ([Position_ID])
);

CREATE TABLE [PRACTICE2].[Prices] (
    [PriceID] INT IDENTITY(1,1) NOT NULL,
    [Asset_ID] INT NOT NULL,
    [Date] DATE NOT NULL,
    [Price_Open] DECIMAL(19,4) NOT NULL,
    [Price_Close] DECIMAL(19,4) NOT NULL,
    [Price_High] DECIMAL(19,4) NOT NULL,
    [Price_Low] DECIMAL(19,4) NOT NULL,
    [Volume] BIGINT,
    CONSTRAINT [pk_prices] PRIMARY KEY ([PriceID])
);