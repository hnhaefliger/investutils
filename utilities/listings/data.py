from .yfinance import get_yfinance_data

def get_ticker_data(ticker):
    return get_yfinance_data(ticker)