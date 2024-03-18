import pyodbc

# Database connection parameters
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEM2040_EOATES'
username = 'EOates'
password = 'DtyV133*831*'

# Connect to the database
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
WITH PortfolioInitialValues AS (
    SELECT
        p.Portfolio_ID,
        MIN(pr.Date) AS Init_Date
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
        p.Portfolio_ID
),
PortfolioCurrentValues AS (
    SELECT
        p.Portfolio_ID,
        p.Portfolio_Name,
        MAX(pr.Date) AS Latest_Date,
        SUM(pos.Quantity * pr.Price_Close) AS Current_Value
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
        p.Portfolio_ID, p.Portfolio_Name
)
SELECT
    cv.Portfolio_ID,
    cv.Portfolio_Name,
    cv.Latest_Date,
    cv.Current_Value,
    piv.Init_Date,
    (SELECT SUM(pos.Quantity * pr.Price_Close)
     FROM [PRACTICE3].[Positions] pos
     JOIN [PRACTICE3].[Prices] pr ON pos.Asset_Symbol = pr.Asset_Symbol AND pr.Date = piv.Init_Date
     WHERE pos.Portfolio_ID = cv.Portfolio_ID) AS Initial_Value
FROM
    PortfolioCurrentValues cv
JOIN
    PortfolioInitialValues piv ON cv.Portfolio_ID = piv.Portfolio_ID
'''

# Execution
cursor = cnxn.cursor()
cursor.execute(Portfolios_Summary)

print(f"Portfolios for {client_name}:")
for row in cursor.fetchall():
    print(f"ID: {row.Portfolio_ID}, Name: {row.Portfolio_Name}, Latest Date: {row.Latest_Date}, Current Value: {row.Current_Value}, Init Date: {row.Init_Date}, Initial Value: {row.Initial_Value}")

# Clean up
cursor.close()
cnxn.close()