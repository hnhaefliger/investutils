from .yfinance import get_yfinance_data, get_chart

def get_ticker_data(ticker):
    return get_yfinance_data(ticker)

def get_ticker_chart(ticker, range, interval):
    return get_chart(ticker, range=range, interval=interval)