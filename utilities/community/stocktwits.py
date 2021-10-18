import requests
import warnings
import random
import json


def try_to_get(dict, *args):
    try:
        for arg in args:
            dict = dict[arg]

        return dict

    except:
        return None


def clean_comment(comment):
    return {
        'id': try_to_get(comment, 'id'),
        'body': try_to_get(comment, 'body'),
        'sentiment': try_to_get(comment, 'entities', 'sentiment', 'basic'),
        'created_at': try_to_get(comment, 'created_at'),
        'source': try_to_get(comment, 'source'),
        'symbols': [try_to_get(symbol, 'symbol') for symbol in comment['symbols']],
        'user': {
            'followers': try_to_get(comment, 'user', 'followers'),
            'following': try_to_get(comment, 'user', 'following'),
            'id': try_to_get(comment, 'user', 'id'),
            'ideas': try_to_get(comment, 'user', 'ideas'),
            'join_date': try_to_get(comment, 'user', 'join_date'),
            'name': try_to_get(comment, 'user', 'name'),
            'username': try_to_get(comment, 'user', 'username'),
        },
    }


def get_comments(ticker, n):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json?filter=top&limit={n}'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()['messages']

    return [clean_comment(comment) for comment in data]


def get_watchlist_count(ticker):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json?filter=top&limit=1'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()['symbol']

    return data['watchlist_count']


def get_top_watched():
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://api.stocktwits.com/api/2/watchlists/top_watched.json'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()

    return data


def get_sentiment(ticker):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://api.stocktwits.com/api/2/symbols/{ticker}/sentiment.json'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()['data']

    return data
    

def get_message_volume(ticker):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://api.stocktwits.com/api/2/symbols/{ticker}/volume.json'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.json()['data']

    return data
