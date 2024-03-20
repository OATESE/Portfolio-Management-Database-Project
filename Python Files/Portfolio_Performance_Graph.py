import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis as currency
def currency_formatter(x, pos):
    return f'${x:,.0f}'

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
client_name = 'Alex Johnson'  # replace with the actual client's name

# SQL query to fetch portfolio performance data for the specified client
sql_query = f'''
SELECT phpv.Portfolio_ID, p.Portfolio_Name, phpv.Date, phpv.PortfolioValue, phpv.CapitalInvested, phpv.ROI
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

    # Apply the currency formatter to the y-axis
    formatter = FuncFormatter(currency_formatter)

    # Plotting the line charts
    portfolio_ids = df['Portfolio_ID'].unique()

    for portfolio_id in portfolio_ids:
        portfolio_df = df[df['Portfolio_ID'] == portfolio_id]
        portfolio_name = portfolio_df['Portfolio_Name'].iloc[0]
        final_roi = portfolio_df['ROI'].iloc[-1] * 100  # Convert ROI to a percentage

        plt.figure(figsize=(14, 7))

        # Plot Capital Invested and Portfolio Value
        plt.plot(portfolio_df['Date'], portfolio_df['CapitalInvested'], label='Capital Invested', marker='o')
        plt.plot(portfolio_df['Date'], portfolio_df['PortfolioValue'], label='Portfolio Value', marker='x')

        # Customizing the plot
        plt.title(f"{portfolio_name} (ID: {portfolio_id}): Capital Invested vs Portfolio Value Over Time")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.gca().yaxis.set_major_formatter(formatter)  # Apply currency formatting to y-axis

        # Neatly format and place the ROI annotation
        roi_annotation = f"Final ROI: {final_roi:.2f}%"
        plt.annotate(roi_annotation, xy=(portfolio_df['Date'].iloc[-1], portfolio_df['PortfolioValue'].iloc[-1]),
                     xytext=(15,15), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

        plt.tight_layout()  # Adjust the plot to ensure everything fits without overlap

        # Show plot
        plt.show()

except Exception as e:
    print(f"An error occurred: {e}")