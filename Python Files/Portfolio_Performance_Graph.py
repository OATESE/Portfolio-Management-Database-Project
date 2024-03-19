import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

# Database connection parameters
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEM2040_EOATES'
username = 'EOates'
password = 'DtyV133*831*'

# Connect to the database
conn_str = f'''
    DRIVER={{ODBC Driver 18 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    TrustServerCertificate=yes;
    Encrypt=no;
'''

# Client's name for whom the portfolios will be fetched
client_name = 'John Doe'  # replace with the actual client's name

# SQL query to fetch portfolio performance data for the specified client
sql_query = f'''
SELECT phpv.Portfolio_ID, p.Portfolio_Name, phpv.Date, phpv.PortfolioValue, phpv.CapitalInvested
FROM [CW1].[PortfolioHistoricalPerformanceView] phpv
JOIN [CW1].[Portfolios] p ON phpv.Portfolio_ID = p.Portfolio_ID
JOIN [CW1].[Clients] c ON p.Client_ID = c.Client_ID
WHERE c.Client_Name = ?
ORDER BY phpv.Portfolio_ID, phpv.Date;
'''

# Connect to the database and fetch the data
try:
    with pyodbc.connect(conn_str) as conn:
        # Fetching the data into a DataFrame
        df = pd.read_sql_query(sql_query, conn, params=[client_name])
    print("Data fetched successfully.")

    # Plotting the line charts
    portfolio_ids = df['Portfolio_ID'].unique()

    for portfolio_id in portfolio_ids:
        portfolio_df = df[df['Portfolio_ID'] == portfolio_id]
        plt.figure(figsize=(14, 7))

        # Plot Capital Invested and Portfolio Value
        plt.plot(portfolio_df['Date'], portfolio_df['CapitalInvested'], label='Capital Invested')
        plt.plot(portfolio_df['Date'], portfolio_df['PortfolioValue'], label='Portfolio Value')

        # Customizing the plot
        plt.title(f"Portfolio ID {portfolio_id}: Capital Invested vs Portfolio Value Over Time")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()  # Adjust the plot to ensure everything fits without overlap

        # Show plot
        plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
