import requests
import warnings
import random

def get_ticker(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(
            f'https://query1.finance.yahoo.com/v6/finance/quote?symbols={ticker}',
            headers=headers, verify=False
        )

    return response.json()