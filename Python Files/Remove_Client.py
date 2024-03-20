import pyodbc

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

import pyodbc

def delete_client_data(client_id, conn_str):
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            
            # Delete related positions first
            cursor.execute('''
                DELETE FROM [CW1].[Positions]
                WHERE Portfolio_ID IN (
                    SELECT Portfolio_ID FROM [CW1].[Portfolios] WHERE Client_ID = ?
                );
            ''', client_id)
            conn.commit()

            # Then delete the portfolios
            cursor.execute('''
                DELETE FROM [CW1].[Portfolios]
                WHERE Client_ID = ?;
            ''', client_id)
            conn.commit()

            # Finally, delete the client
            cursor.execute('''
                DELETE FROM [CW1].[Clients]
                WHERE Client_ID = ?;
            ''', client_id)
            conn.commit()

            print(f"All data deleted for Client ID {client_id}.")
    except Exception as e:
        print(f"An error occurred while deleting client data: {e}")

# Example usage:
delete_client_data(client_id=15, conn_str=connection_string)
