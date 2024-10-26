import yfinance as yf
import pandas as pd

# Get portfolio csv and put into dataframe

df = pd.read_csv('portfolio.csv')
df_ira = pd.read_csv('portfolio_ira.csv')

# Function to fetch the current stock price using yfinance
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'].iloc[-1]  # Get the latest closing price
    return price

# Create a new column 'Equity' by fetching the stock price and multiplying by share count
def add_equity_column(df):
    df['Equity'] = df.apply(lambda row: get_stock_price(row['Ticker']) * row['Shares'], axis=1)
    df['Equity'] = round(df['Equity'], 2)

# Print total equity
def print_equity(df):
    print(f'Total: ${round(df["Equity"].sum(), 2)}')

add_equity_column(df)
add_equity_column(df_ira)

print(df)
print_equity(df)

print(df_ira)
print_equity(df_ira)





'''

# Define the stock ticker symbol
ticker_symbol = "AAPL"  # Replace with your desired stock symbol

# Get stock data
stock = yf.Ticker(ticker_symbol)

# Download today's stock data, including extended hours
data = stock.history(period="1d", interval="30m")
print(data['Open'].iloc[0])
print(data['Close'].iloc[0])


# Get the last row which typically includes the latest available price, including after-hours if the market is closed
last_price = data['Close'][-1]

print(f"After-hours price of {ticker_symbol} is: ${last_price:.2f}")

'''