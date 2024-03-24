Sure, here's how you could document the logical database design and the normalization checks for each table in Markdown:


# Financial Portfolio Database - Logical Design

## Logical Database Design (Bracketed Notation)

### Clients Table
```
Clients (Client_ID, Client_Name, Client_Email, Client_Number)
    Primary key (Client_ID)
```
- **1NF**: The table has a primary key (Client_ID) and there are no repeating groups. All attributes have their own columns and are of a single value, meeting 1NF criteria.
- **2NF**: Since there is only one primary key and no composite primary key, there can't be a partial dependency. The table is in 2NF.
- **3NF**: All attributes are only dependent on the primary key (Client_ID), with no transitive dependencies present. The table is in 3NF.
  
### Portfolios Table
```
Portfolios (Portfolio_ID, Client_ID, Portfolio_Name, Portfolio_Description, Portfolio_Purpose, Portfolio_Init_Date)
    Primary key (Portfolio_ID)
    Foreign key (Client_ID) references Clients (Client_ID) on Update Cascade on Delete Set Null
```
- **1NF**: The table has a primary key (Portfolio_ID) with no repeating groups. All data is atomic.
- **2NF**:  Since there is only one primary key and no composite primary key, there can't be a partial dependency. The table is in 2NF.
- **3NF**: The Client_ID is a foreign key; all other attributes depend only on the primary key. The table is in 3NF

### Assets Table
```
Assets (AssetID, Asset_Type, AssetSymbol, Asset_Name, Industry)
    Primary key (AssetSymbol)
```
- **1NF**:The table has a primary key (AssetSymbol) with no repeating groups. All data is atomic.
- **2NF**: With a single field as the primary key, the table is in 2NF because there's no possibility of partial dependency.
- **3NF**:There are no transitive dependencies as all non-key fields depend only on the primary key. The table is in 3NF.
```
Positions (Position_ID, Portfolio_ID, Asset_Symbol, Quantity, PurchaseDate, PurchasePrice, CurrentPrice)
    Primary key (Position_ID)
    Foreign key (Portfolio_ID) references Portfolios (Portfolio_ID) on Update Cascade on Delete Cascade
    Foreign key (Asset_Symbol) references Assets (AssetSymbol) on Update Cascade on Delete Restrict
```
- **1NF**: The table has a primary key (Position_ID) with no repeating groups. All data is atomic.
- **2NF**: There's only one primary key, so no partial dependency can exist. The table is in 2NF
- **3NF**: PurchasePrice and CurrentPrice depend only on the Position_ID (each position has its own purchase price and current price), and there are no transitive dependencies. The table is in 3NF.

### Prices Table
```
Prices (PriceID, Asset_Symbol, Date, Price_Open, Price_Close, Price_High, Price_Low, Volume)
    Primary key (PriceID)
    Foreign key (Asset_Symbol) references Assets (AssetSymbol) on Update Cascade on Delete Restrict
```
- **1NF**: The table has a primary key (PriceID) and no repeating groups. All data is atomic.
- **2NF**: There's a single field primary key, so there are no partial dependencies. The table is in 2NF.
- **3NF**: All non-key attributes are only dependent on the primary key and there are no transitive dependencies. The table is in 3NF.


