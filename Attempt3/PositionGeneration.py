import random
from datetime import timedelta, date

# Provided dictionary for client and their portfolios
client_portfolio_dict = {
    1: [1],
    2: [2],
    3: [3, 4],
    4: [5],
    5: [6],
    6: [7, 8],
    7: [9],
    8: [10],
    9: [11, 12],
    10: [13],
    11: [14],
    12: [15, 16],
    13: [17],
    14: [18],
    15: [19, 20]
}

# Function to generate random dates within a range
def random_dates(start_date, end_date, num_dates):
    delta = end_date - start_date
    random_dates = [start_date + timedelta(days=random.randrange(delta.days)) for _ in range(num_dates)]
    return random_dates

# Adjusted function to generate random asset positions, ensuring correct client-portfolio assignment
def generate_positions(client_portfolio_dict, asset_symbols, start_date, end_date, num_positions_per_portfolio):
    positions = []
    for client_id, portfolio_ids in client_portfolio_dict.items():
        for portfolio_id in portfolio_ids:
            for _ in range(num_positions_per_portfolio):
                asset_symbol = random.choice(asset_symbols)
                quantity = random.randint(1, 100)  # example quantity range
                purchase_date = random.choice(random_dates(start_date, end_date, 1))        
                position = (portfolio_id, client_id, asset_symbol, quantity, purchase_date)
                positions.append(position)
    
    return positions

# Function to convert positions to a single SQL insert statement
def positions_to_insert_sql(positions, table_name, schema_name='dbo'):
    insert_stmt = f"INSERT INTO [{schema_name}].[{table_name}] (Portfolio_ID, Client_ID, Asset_Symbol, Quantity, PurchaseDate) VALUES "
    values_list = ["(" + ', '.join([
                    str(position[0]),  # Portfolio_ID
                    str(position[1]),  # Client_ID
                    f"'{position[2]}'",  # Asset_Symbol
                    str(position[3]),  # Quantity
                    f"'{position[4].strftime('%Y-%m-%d')}'"  # PurchaseDate
                   ]) + ")" for position in positions]
    insert_stmt += ',\n'.join(values_list) + ";"
    return insert_stmt

# Usage
asset_symbols = [
    'AAPL', 'ABBV', 'AMD', 'AMZN', 'AUDUSD=X', 'BAC', 'BCH-USD', 'BTC-USD',
    'C', 'CL=F', 'COP', 'CVX', 'EEM', 'EOG', 'ETH-USD', 'EURUSD=X',
    'GBPUSD=X', 'GC=F', 'GILD', 'GM', 'GOOGL', 'GS', 'HD', 'HYG', 'JNJ',
    'JPM', 'LTC-USD', 'MRK', 'MS', 'MSFT', 'NG=F', 'NKE', 'NVDA', 'NZDUSD=X',
    'PFE', 'QQQ', 'SI=F', 'SLB', 'SPY', 'TSLA', 'USDCAD=X', 'USDCHF=X',
    'USDJPY=X', 'USDNOK=X', 'USDSEK=X', 'VEA', 'VGLT', 'VTI', 'XOM', 'XRP-USD'
]
start_date = date(2023, 1, 1)
end_date = date(2023, 2, 28)
num_positions_per_portfolio = 30  # Adjust the number of positions as needed

# Generate positions with correct portfolio assignment
positions = generate_positions(client_portfolio_dict, asset_symbols, start_date, end_date, num_positions_per_portfolio)

# Convert positions to SQL insert statements
insert_sql = positions_to_insert_sql(positions, 'Positions', 'PRACTICE3')

# Print the SQL insert statements
print(insert_sql)