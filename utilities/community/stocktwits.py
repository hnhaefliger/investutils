import requests
import warnings
import random


def clean_comment(comment):
    return {
        'id': comment['id'],
        'body': comment['body'],
        'sentiment': comment['entities']['sentiment'],
        'created_at': comment['created_at'],
        'source': comment['source'],
        'symbols': [symbol['symbol'] for symbol in comment['symbol']],
        'user': {
            'followers': comment['user']['followers'],
            'following': comment['user']['following'],
            'id': comment['user']['id'],
            'ideas': comment['user']['ideas'],
            'join_date': comment['user']['join_date'],
            'name': comment['user']['name'],
            'username': comment['user']['username'],
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
