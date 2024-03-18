import pandas as pd
import pyodbc

##Client Name
client_name = 'John Doe'


# Database connection parameters
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEM2040_EOATES'
username = 'EOates'
password = 'DtyV133*831*'

# Connect to the database
connection_string = f'''
    DRIVER={{ODBC Driver 18 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    TrustServerCertificate=yes;
    Encrypt=no;
'''

# SQL query

sql_query = f'''
SELECT
    p.Portfolio_ID,
    p.Portfolio_Name,
    pr.Date,
    SUM(pos.Quantity * pr.Price_Close) AS Portfolio_Value,
    SUM(CASE WHEN pos.PurchaseDate <= pr.Date THEN pos.Quantity * pos.PurchasePrice ELSE 0 END) AS Amount_Invested_Up_To_Date
FROM
    [PRACTICE3].[Clients] c
JOIN
    [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
JOIN
    [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
JOIN
    [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol AND pos.PurchaseDate <= pr.Date
WHERE
    c.Client_Name = '{client_name}'
GROUP BY
    p.Portfolio_ID, p.Portfolio_Name, pr.Date
ORDER BY
    p.Portfolio_ID, pr.Date;
'''

try:
    # Establishing connection
    cnxn = pyodbc.connect(connection_string)
    print("Connected to the database successfully.")

    # Executing the query and loading into a DataFrame
    df = pd.read_sql_query(sql_query, cnxn)

    # Displaying the DataFrame
    print(df)

except Exception as e:
    print(f"Error: {e}")
finally:
    # Ensuring the connection is closed
    cnxn.close()


import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame from the previous code

# Get unique portfolio IDs
portfolio_ids = df['Portfolio_ID'].unique()

# Create a plot for each portfolio ID
for portfolio_id in portfolio_ids:
    portfolio_df = df[df['Portfolio_ID'] == portfolio_id]
    portfolio_name = portfolio_df['Portfolio_Name'].iloc[0]

    # Calculate ROI for the most recent date
    # Ensure the DataFrame is sorted by Date if it's not already
    portfolio_df = portfolio_df.sort_values(by='Date')
    most_recent_portfolio_value = portfolio_df['Portfolio_Value'].iloc[-1]
    most_recent_invested_amount = portfolio_df['Amount_Invested_Up_To_Date'].iloc[-1]
    if most_recent_invested_amount > 0:  # Prevent division by zero
        roi = (most_recent_portfolio_value / most_recent_invested_amount) - 1
        roi_percentage = roi * 100  # Convert to percentage
    else:
        roi_percentage = 0

    # Create a new figure for each portfolio
    plt.figure(figsize=(10, 6))
    
    # Plotting portfolio value
    plt.plot(portfolio_df['Date'], portfolio_df['Portfolio_Value'], marker='', color='blue', linewidth=2.5, label='Portfolio Value')
    
    # Plotting amount invested up to date
    plt.plot(portfolio_df['Date'], portfolio_df['Amount_Invested_Up_To_Date'], marker='', color='red', linewidth=2.5, linestyle='dashed', label='Amount Invested Up To Date')
    
    # Customizing the plot
    plt.title(f'Portfolio Value and Amount Invested Over Time\n{portfolio_name} (ID: {portfolio_id})')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    # Annotating ROI on the most recent date
    plt.annotate(f'ROI: {roi_percentage:.2f}%', xy=(1, 0), xycoords='axes fraction', fontsize=12,
                 xytext=(-10, 10), textcoords='offset points',
                 ha='right', va='bottom')

    # Show plot
    plt.show()
