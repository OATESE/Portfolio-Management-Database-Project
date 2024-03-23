| **UNF**                  | **1nf**               | **2nf**               | **3nf**               | **TABLES** |
|--------------------------|-----------------------|-----------------------|-----------------------|------------|
| Client_ID                | _Client_ID_           | _Client_ID_           | _Client_ID_           | Clients    |
| Client_Name              | Client_Name           | Client_Name           | Client_Name           |            |
| Client_Email             | Client_Email          | Client_Email          | Client_Email          |            |
| Client_Number            | Client_Number         | Client_Number         | Client_Number         |            |
|    (Portfolio_ID         |                       |                       |                       |            |
|    Portfolio_Name        | _Portfolio_ID_       | _Portfolio_ID_       | _Portfolio_ID_       | Portfolios |
|    Portfolio_Description | Client_ID             | Client_ID             | Client_ID             |            |
|    Portfolio_Purpose     | Portfolio_Name        | Portfolio_Name        | Portfolio_Name        |            |
|    Portfolio_Init_Date   | Portfolio_Description | Portfolio_Description | Portfolio_Description |            |
|    (AssetSymbol          | Portfolio_Purpose     | Portfolio_Purpose     | Portfolio_Purpose     |            |
|       Asset_Type         | Portfolio_Init_Date   | Portfolio_Init_Date   | Portfolio_Init_Date   |            |
|       AssetID            |                       |                       |                       |            |
|       Asset_Name         | _AssetSymbol_         | _AssetSymbol_         | _AssetSymbol_         | Assets     |
|       Industry           | Portfolio_ID          | Portfolio_ID          | Portfolio_ID          |            |
|       (Position_ID       | Asset_Type            | Asset_Type            | Asset_Type            |            |
|          Quantity        | AssetID               | AssetID               | AssetID               |            |
|          PurchaseDate    | Asset_Name            | Asset_Name            | Asset_Name            |            |
|          PurchasePrice   | Industry              | Industry              | Industry              |            |
|          CurrentPrice    |                       |                       |                       |            |
|          (PriceID        | _Position_ID_         | _Position_ID_         | _Position_ID_         | Position   |
|             Date         | AssetID               | AssetID               | AssetID               |            |
|             Price_Open   | Quantity              | Quantity              | Quantity              |            |
|             Price_Close  | PurchaseDate          | PurchaseDate          | PurchaseDate          |            |
|             Price_High   | PurchasePrice         | PurchasePrice         | PurchasePrice         |            |
|             Price_Low    | CurrentPrice          | CurrentPrice          | CurrentPrice          |            |
|             Volume))))   |                       |                       |                       |            |
|                          | _PriceID_             | _PriceID_             | _PriceID_             | Prices     |
|                          | AssetID               | AssetID               | AssetID               |            |
|                          | Date                  | Date                  | Date                  |            |
|                          | Price_Open            | Industry              | Price_Open            |            |
|                          | Price_Close           | Price_Close           | Price_Close           |            |
|                          | Price_High            | Price_High            | Price_High            |            |
|                          | Price_Low             | Price_Low             | Price_Low             |            |
|                          | Volume                | Volume                | Volume                |            |
