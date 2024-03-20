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
client_name = 'Alex Johnson' 
# SQL query to fetch asset allocation data for the specified client
sql_query = f'''
SELECT p.Portfolio_ID, aav.Date, 
    aav.EquityProportion, aav.BondProportion, aav.CommodityProportion, 
    aav.CurrencyProportion, aav.ETFProportion, aav.MutualFundProportion, 
    aav.OptionProportion, aav.FutureProportion, aav.CryptocurrencyProportion
FROM [CW1].[AssetAllocationView2] aav
JOIN [CW1].[Portfolios] p ON aav.Portfolio_ID = p.Portfolio_ID
JOIN [CW1].[Clients] c ON p.Client_ID = c.Client_ID
WHERE c.Client_Name = ?
ORDER BY aav.Portfolio_ID, aav.Date;
'''

# Connect to the database and fetch the data
try:
    with pyodbc.connect(conn_str) as conn:
        df = pd.read_sql_query(sql_query, conn, params=[client_name])

    # Fetching the data into a DataFrame
    print("Data fetched successfully.")

    # Get unique portfolio IDs
    portfolio_ids = df['Portfolio_ID'].unique()

    # Plotting the distribution of asset classes for each portfolio
    for portfolio_id in portfolio_ids:
        # Filter the DataFrame for the current portfolio ID
        portfolio_df = df[df['Portfolio_ID'] == portfolio_id]

        plt.figure(figsize=(14, 7))

        # Plot stacked area chart for asset class distribution
        plt.stackplot(portfolio_df['Date'],
                      portfolio_df['EquityProportion'],
                      portfolio_df['BondProportion'],
                      portfolio_df['CommodityProportion'],
                      portfolio_df['CurrencyProportion'],
                      portfolio_df['ETFProportion'],
                      portfolio_df['MutualFundProportion'],
                      portfolio_df['OptionProportion'],
                      portfolio_df['FutureProportion'],
                      portfolio_df['CryptocurrencyProportion'],
                      labels=['Equity', 'Bond', 'Commodity', 'Currency', 'ETF', 'Mutual Fund', 'Option', 'Future', 'Cryptocurrency'])

        # Customizing the plot
        plt.title(f"Portfolio ID {portfolio_id}: Asset Class Distribution Over Time")
        plt.xlabel('Date')
        plt.ylabel('Proportion')
        plt.legend(loc='upper left')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
