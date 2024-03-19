import yfinance as yf
import pandas as pd
#usage
symbols = [
    'AAPL', 'ABBV', 'AMD', 'AMZN', 'AUDUSD=X', 'BAC', 'BCH-USD', 'BTC-USD',
    'C', 'CL=F', 'COP', 'CVX', 'EEM', 'EOG', 'ETH-USD', 'EURUSD=X',
    'GBPUSD=X', 'GC=F', 'GILD', 'GM', 'GOOGL', 'GS', 'HD', 'HYG', 'JNJ',
    'JPM', 'LTC-USD', 'MRK', 'MS', 'MSFT', 'NG=F', 'NKE', 'NVDA', 'NZDUSD=X',
    'PFE', 'QQQ', 'SI=F', 'SLB', 'SPY', 'TSLA', 'USDCAD=X', 'USDCHF=X',
    'USDJPY=X', 'USDNOK=X', 'USDSEK=X', 'VEA', 'VGLT', 'VTI', 'XOM', 'XRP-USD'
]
start_date = '2023-01-01'
end_date = '2024-3-19'
def download_prices_for_symbols(symbols, start_date, end_date):
    all_data = []  # A list to hold data from each symbol
    
    for symbol in symbols:
        # Download stock data from yfinance for each symbol
        data = yf.download(symbol, start=start_date, end=end_date)
        
        # Check if data is empty
        if not data.empty:
            # Reset the index to turn the Date index into a column
            data.reset_index(inplace=True)
            
            # Drop the 'Adj Close' column as it's not needed
            data.drop('Adj Close', axis=1, inplace=True)

            # Insert a new column with the symbol
            data.insert(1, 'Asset_Symbol', symbol)  # Insert at position 1 to keep Date as the first column

            # Append the data to the all_data list
            all_data.append(data)
    
    # Concatenate all DataFrames in the list into a single DataFrame
    combined_data = pd.concat(all_data)
    
    return combined_data

prices_df = download_prices_for_symbols(symbols, start_date, end_date)

def df_to_batch_insert_sql(df, table_name, schema_name='dbo'):
    grouped_df = df.groupby('Asset_Symbol')
    insert_stmts = []

    for symbol, group in grouped_df:
        # We don't need to reorder or rename since the DataFrame already matches the database schema.
        vals_list = []
        for index, row in group.iterrows():
            # Ensure the date is formatted as a string 'YYYY-MM-DD'
            date_str = row['Date'].strftime('%Y-%m-%d')
            # Prepare the value strings, making sure to format the date correctly
            vals = f"'{symbol}', '{date_str}', {row['Open']}, {row['High']}, {row['Low']}, {row['Close']}, {row['Volume']}"
            vals_list.append(f"({vals})")
        vals_str = ',\n'.join(vals_list)
        stmt = f"INSERT INTO [{schema_name}].[{table_name}] ([Asset_Symbol], [Date], [Price_Open], [Price_High], [Price_Low], [Price_Close], [Volume]) VALUES \n{vals_str};"
        insert_stmts.append(stmt)
    
    return insert_stmts

# Assuming prices_df is your DataFrame from the previous function
table_name = 'Prices'
schema_name = 'CW1'
sql_statements = df_to_batch_insert_sql(prices_df, table_name, schema_name)

# Print the SQL insert statements
for stmt in sql_statements:
    print(stmt)