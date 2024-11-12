from flask import Flask, render_template_string
import yfinance as yf
import threading
import time

app = Flask(__name__)

ticker = 'AAPL'  # Apple Inc.
stock_price = 0.0

def fetch_stock_price():
    global stock_price
    while True:
        stock = yf.Ticker(ticker)
        stock_info = stock.history(period='1d')
        stock_price = stock_info['Close'].iloc[-1]
        time.sleep(1)  # Refresh every 10 seconds

@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Stock Ticker</title>
            <script>
                setInterval(function() {
                    fetch('/price')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('price').textContent = 'Price: ' + data.price;
                    });
                }, 1000);  // Refresh every 10 seconds
            </script>
        </head>
        <body>
            <h1>Stock Ticker: {{ ticker }}</h1>
            <p id="price">Price: {{ price }}</p>
        </body>
        </html>
    ''', ticker=ticker, price=stock_price)

@app.route('/price')
def price():
    return {'price': stock_price}

if __name__ == '__main__':
    threading.Thread(target=fetch_stock_price, daemon=True).start()
    app.run(port=5000)
