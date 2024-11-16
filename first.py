import yfinance as yf
import time

def get_stock_price(ticker):
    stock = yf.Ticker(ticker) 
    stock_info = stock.history(period='1d')
    return stock_info['Close'].iloc[-1]

def refresh_stock_price(ticker, interval):
    while True:
        price = get_stock_price(ticker)
        print(f'Ticker: {ticker} | Price: {price}') 
        time.sleep(interval)

ticker = 'BTC-USD'# Bitcoin currency
interval = 1 # Refresh every 1 seconds

refresh_stock_price(ticker, interval)
