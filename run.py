# import yfinance as yf

# # Define the stock ticker symbol
# ticker_symbol = "AAPL"  # Replace with the desired stock symbol

# # Get stock data
# stock = yf.Ticker(ticker_symbol)

# # Get the current stock price
# current_price = stock.history(period="1d")['Close'][0]

# print(f"Current price of {ticker_symbol} is: ${current_price:.2f}")

import yfinance as yf

# Define the stock ticker symbol
ticker_symbol = "AAPL"  # Replace with your desired stock symbol

# Get stock data
stock = yf.Ticker(ticker_symbol)

# Download today's stock data, including extended hours
data = stock.history(period="1d", interval="30m")
print(data['Open'].iloc[0])
print(data['Close'].iloc[0])


'''
# Get the last row which typically includes the latest available price, including after-hours if the market is closed
last_price = data['Close'][-1]

print(f"After-hours price of {ticker_symbol} is: ${last_price:.2f}")

'''