import requests
import random
import warnings


def stock_on_robinhood(stock):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(f'https://robinhood.com/stocks/{stock}', headers=headers, verify=False)

    return response.status_code == 200

def on_robinhood(ticker, ticker_type):
    if ticker_type == 'EQUITY':
        return stock_on_robinhood(ticker)

    else:
        return False
