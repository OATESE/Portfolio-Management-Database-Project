import pyodbc

# Database connection parameters
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEM2040_EOATES'
username = 'EOates'
password = 'DtyV133*831*'

conn_str = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'TrustServerCertificate=yes;'
    'Encrypt=no;'
)

# SQL to insert a new position
insert_query = f'''
INSERT INTO [CW1].[Positions] (Portfolio_ID, Asset_Symbol, Quantity, PurchaseDate, PurchasePrice)
VALUES (?, ?, ?, ?, ?);
'''
# Function to create a new position
def create_position(conn_str, portfolio_id, asset_symbol, quantity, purchase_date, purchase_price):
    try:
        # Establishing the database connection
        with pyodbc.connect(conn_str) as conn:
            with conn.cursor() as cursor:
                # Executing the insert query
                cursor.execute(insert_query, portfolio_id, asset_symbol, quantity, purchase_date, purchase_price)
                # Committing the transaction
                conn.commit()
                print("Position created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Trade details
portfolio_id = 2  # The ID of the portfolio where the position will be added
asset_symbol = 'AAPL'  # Symbol for the asset being traded
quantity = 10  # Number of units being traded
purchase_price = 150.00  # Price at which the units were bought
purchase_date = '2024-01-01'  # The date of the trade

# Call the function to create a new position
create_position(conn_str, portfolio_id, asset_symbol, quantity, purchase_date, purchase_price)