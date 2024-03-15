import yfinance as yf 
from datetime import datetime
# Define the start and end date for the data download
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

tickers = yf.Tickers('SPY MSFT AAPL')
print (tickers.tickers['MSFT'].info)

