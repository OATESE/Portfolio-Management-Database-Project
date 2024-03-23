## CRUD Operation Files

### Portfolio_Asset_Allocation_over_Time.py
- This script generates a time-series area chart displaying the relative allocation of different asset classes in a portfolio over time.

### Portfolio_Performance_Graph.py
- A Python script that creates a graph to track the performance of a portfolio, comparing capital invested versus portfolio value across a timeline.

### Register_Long_Trade.py
- This script is used to register a new trade, specifically a long position, adding it to an existing portfolio.

### Remove_Client.py
- This script removes a client from the database, including all associated data, typically used for clients who are no longer using the investement service.

### Update_Client_Info.py
- A script to update the contact information of existing clients in the database, such as email or phone number.

### Update_Position_Size.py
- This script adjusts the size of an existing investment position, such as increasing or decreasing the number of shares held.

These scripts demonstrate the ability to perform Create, Read, Update, and Delete (CRUD) operations on a financial portfolio database using Python. Each script is to a specific operation relevant to managing a client's financial portfolio.

## Data Generating Files
These are two files that i used to populate the prices and position tables as these would require a much larger amount of initial rows than what would be feasible manualy. I did not choose to do this with the pyodbc driver as i needed data in the tables before i was working on that part of the project. 


### PricesDataInsert.py  
- This script uses the yfinance api to download historical prices for a given set of asset symbols over a specified date range. It then Prints an insert statement for each asset symbol so that the the sql data insert query can be easily copied rather than writing several thousands of lines manualy. I found that this is more effective especially when using several asset symbols (tickers) to run this in a jupyter notebook rather than vscode vscode output in terminal is limited. 

### POsitionDataInsert,py
- This script generates insert statement for randomly generate positions for a set amount of portfolios. The amount of positions to be generated over a given timeframe can be changed. 
