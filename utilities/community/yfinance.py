import requests
import warnings
import random


def get_trending(n, region='US'):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://query2.finance.yahoo.com/v1/finance/trending/{region}?count={n}'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()['finance']['result'][0]['quotes']

    return [symbol['symbol'] for symbol in data]


def get_related(n, ticker):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://query2.finance.yahoo.com/v6/finance/recommendationsbysymbol/{ticker}?count={n}'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()['finance']['result']

    return data