import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

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
sql_query = '''
WITH PortfolioValues AS (
    SELECT
        p.Portfolio_ID,
        pr.Date,
        a.Asset_Type,
        pos.Quantity * pr.Price_Close AS AssetTypeValue
    FROM
        [PRACTICE3].[Clients] c
    JOIN [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
    JOIN [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN [PRACTICE3].[Assets] a ON pos.Asset_Symbol = a.AssetSymbol
    JOIN [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol AND pos.PurchaseDate <= pr.Date
    WHERE
        c.Client_Name = 'Alex Johnson'
),
PortfolioTotalValues AS (
    SELECT
        Portfolio_ID,
        Date,
        SUM(AssetTypeValue) AS TotalValue
    FROM PortfolioValues
    GROUP BY Portfolio_ID, Date
)
SELECT
    pvt.Portfolio_ID,
    pvt.Date,
    ISNULL([Equity] / ptv.TotalValue, 0) AS StockProportion,
    ISNULL([Bond] / ptv.TotalValue, 0) AS BondProportion,
    ISNULL([Commodity] / ptv.TotalValue, 0) AS CommodityProportion,
    ISNULL([Currency] / ptv.TotalValue, 0) AS CurrencyProportion,
    ISNULL([ETF] / ptv.TotalValue, 0) AS ETFProportion,
    ISNULL([MutualFund] / ptv.TotalValue, 0) AS MFProportion,
    ISNULL([Option] / ptv.TotalValue, 0) AS OptionProportion,
    ISNULL([Future] / ptv.TotalValue, 0) AS FutureProportion,
    ISNULL([Cryptocurrency] / ptv.TotalValue, 0) AS CryptoProportion
FROM
    PortfolioValues pv
PIVOT (
    SUM(AssetTypeValue)
    FOR Asset_Type IN ([Equity], [Bond], [Commodity], [Currency], [ETF], [MutualFund], [Option], [Future], [Cryptocurrency])
) AS pvt
JOIN PortfolioTotalValues ptv ON pvt.Portfolio_ID = ptv.Portfolio_ID AND pvt.Date = ptv.Date
ORDER BY
    pvt.Portfolio_ID, pvt.Date;
'''


try:
    cnxn = pyodbc.connect(connection_string)
    print("Connected to the database successfully.")
    
    # Fetching data into DataFrame
    df = pd.read_sql_query(sql_query, cnxn)
    print("Data retrieved successfully.")

except Exception as e:
    print(f"Error: {e}")

#finally:
    cnxn.close()

df.sort_values(by=['Portfolio_ID', 'Date'], inplace=True)

# Plotting
portfolio_ids = df['Portfolio_ID'].unique()

for portfolio_id in portfolio_ids:
    portfolio_data = df[df['Portfolio_ID'] == portfolio_id]
    plt.figure(figsize=(14, 7))
    
    # Plot each asset type proportion as a separate line
    for column in portfolio_data.columns[3:]:  # Skip 'Portfolio_ID', 'Date', 'TotalValue'
        plt.plot(portfolio_data['Date'], portfolio_data[column], label=column)
    
    plt.title(f'Asset Class Proportions Over Time for Portfolio ID {portfolio_id}')
    plt.xlabel('Date')
    plt.ylabel('Proportion')
    plt.legend()
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()