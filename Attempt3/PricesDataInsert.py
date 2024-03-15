import yfinance as yf
import pandas as pd


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

# Display the combined DataFrame to verify

#usage
symbols = ['AAPL', 'MSFT', 'GOOGL']
start_date = '2023-01-01'
end_date = '2023-12-31'
prices_df = download_prices_for_symbols(symbols, start_date, end_date)

#prices_df

def df_to_batch_insert_sql(df, table_name, schema_name='dbo'):
    grouped_df = df.groupby('Asset_Symbol')
    insert_stmts = []
    
    for symbol, group in grouped_df:
        cols = ', '.join([f"[{col}]" for col in group.columns])
        vals_list = []
        for index, row in group.iterrows():
            vals = ', '.join([f"'{row[col]}'" if isinstance(row[col], str)
                              else ("CONVERT(DATE, '" + str(row[col])[:10] + "', 120)" if col == 'Date' 
                                    else str(row[col])) for col in group.columns])
            vals_list.append(f"({vals})")
        vals_str = ',\n'.join(vals_list)
        stmt = f"INSERT INTO [{schema_name}].[{table_name}] ({cols}) VALUES \n{vals_str};"
        insert_stmts.append(stmt)
    
    return insert_stmts

# Assuming prices_df is your DataFrame from the previous function
table_name = 'Prices'
schema_name = 'PRACTICE3'
sql_statements = df_to_batch_insert_sql(prices_df, table_name, schema_name)

# Print the SQL insert statements
for stmt in sql_statements:
    print(stmt)