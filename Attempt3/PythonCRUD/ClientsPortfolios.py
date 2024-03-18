import pyodbc

# Database connection parameters
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEM2040_EOATES'
username = 'EOates'
password = 'DtyV133*831*'

# Attempt to connect to the database
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                          f'SERVER={server};'
                          f'DATABASE={database};'
                          f'UID={username};'
                          f'PWD={password};'
                          'TrustServerCertificate=yes;'
                          'Encrypt=no;')
    print("Connected to the database successfully.")
except Exception as e:
    print("Error connecting to the database:", e)
    exit()



client_name = 'John Doe'  # Client name to search for

Portfolios_Summary = f'''
WITH PortfolioValues AS (
    SELECT
        p.Client_ID,
        p.Portfolio_ID,
        p.Portfolio_Name,
        pr.Date,
        SUM(pos.Quantity * pr.Price_Close) AS Total_Value,
        ROW_NUMBER() OVER(PARTITION BY p.Portfolio_ID ORDER BY pr.Date DESC) AS rn
    FROM
        [PRACTICE3].[Clients] c
    JOIN
        [PRACTICE3].[Portfolios] p ON c.Client_ID = p.Client_ID
    JOIN
        [PRACTICE3].[Positions] pos ON p.Portfolio_ID = pos.Portfolio_ID
    JOIN
        [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol
    WHERE
        c.Client_Name = '{client_name}'
    GROUP BY
        p.Client_ID, p.Portfolio_ID, p.Portfolio_Name, pr.Date
)
SELECT
    Portfolio_ID, Portfolio_Name, Date, Total_Value
FROM
    PortfolioValues
WHERE
    rn = 1;
'''

##Execution
cursor = cnxn.cursor()
cursor.execute(Portfolios_Summary)

print(f"Portfolios for {client_name}:")
for row in cursor.fetchall():
    print(f"ID: {row.Portfolio_ID}, Name: {row.Portfolio_Name}, Date: {row.Date}, Value: {row.Total_Value}")

# Clean up
cursor.close()
cnxn.close()




