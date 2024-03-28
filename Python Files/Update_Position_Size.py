import pyodbc

# Database connection parameters
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEM2040_EOATES'
username = 'EOates'
password = 

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

def update_position_size(position_id, new_quantity, conn_str):
    update_query = '''
        UPDATE [CW1].[Positions]
        SET Quantity = ?
        WHERE Position_ID = ?;
    '''
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(update_query, new_quantity, position_id)
            conn.commit()
            print(f"Position size updated for Position ID {position_id}.")
    except Exception as e:
        print(f"An error occurred while updating position size: {e}")


# Example usage:
update_position_size(position_id=123, new_quantity=150, conn_str=connection_string)
