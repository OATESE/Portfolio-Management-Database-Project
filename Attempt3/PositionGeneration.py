import random
from datetime import timedelta, date

# Function to generate random dates within a range
def random_dates(start_date, end_date, num_dates):
    delta = end_date - start_date
    random_dates = [start_date + timedelta(days=random.randrange(delta.days)) for _ in range(num_dates)]
    return random_dates

# Function to generate random asset positions
def generate_positions(client_ids, asset_symbols, start_date, end_date, num_positions_per_portfolio):
    positions = []
    for client_id in client_ids:
        for _ in range(num_positions_per_portfolio):
            portfolio_id = random.choice(range(1, num_positions_per_portfolio + 1))  # assuming portfolio IDs are sequential and start at 1
            asset_symbol = random.choice(asset_symbols)
            quantity = random.randint(10, 100)  # example quantity range
            purchase_dates = random_dates(start_date, end_date, 1)
            purchase_price = round(random.uniform(10, 500), 2)  # example price range
            current_price = round(purchase_price * random.uniform(0.9, 1.1), 2)  # fluctuate the price a bit
            
            position = (portfolio_id, client_id, asset_symbol, quantity, purchase_dates[0], purchase_price, current_price)
            positions.append(position)
    
    return positions

#Usage
client_ids = range(1, 16)  # Client IDs 1 through 15
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
num_positions_per_portfolio = 5  # number of positions per portfolio

# Generate positions
positions = generate_positions(client_ids, asset_symbols, start_date, end_date, num_positions_per_portfolio)

# Print the positions to verify
for position in positions:
    print(position)

def positions_to_insert_sql(positions, table_name, schema_name='dbo'):
    # Start the INSERT statement
    insert_stmt = f"INSERT INTO [{schema_name}].[{table_name}] (Portfolio_ID, Client_ID, Asset_Symbol, Quantity, PurchaseDate, PurchasePrice, CurrentPrice) VALUES "
    # Create the VALUES part of the statement with all position values
    values_list = []
    for position in positions:
        values_list.append(
            "(" +
            ', '.join([
                f"'{v}'" if isinstance(v, str) else
                f"'{v.strftime('%Y-%m-%d')}'" if isinstance(v, date) else
                str(v)
                for v in position]) +
            ")"
        )
    # Combine the individual VALUES parts into one string separated by commas
    insert_stmt += ', '.join(values_list) + ";"
    return insert_stmt

# Convert positions to a single SQL insert statement
insert_sql = positions_to_insert_sql(positions, 'Positions', 'PRACTICE3')

# Print the SQL insert statement
print(insert_sql)
