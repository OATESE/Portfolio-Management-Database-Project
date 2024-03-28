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

def update_client_information(client_id, new_name, new_contact_info, conn_str):
    update_query = '''
        UPDATE [CW1].[Clients]
        SET Client_Name = ?, Client_Email = ?
        WHERE Client_ID = ?;
    '''
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(update_query, new_name, new_contact_info, client_id)
            conn.commit()
            print(f"Client information updated for Client ID {client_id}.")
    except Exception as e:
        print(f"An error occurred while updating client information: {e}")

# Example usage:
update_client_information(client_id=1, new_name='Jane Doe', new_contact_info='JaneDoe@email.com', conn_str=connection_string)
