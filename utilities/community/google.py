import requests
import warnings
import random
import re


def clean_article(article):
    return {
        'title': re.findall('<title>(.+?)</title>', article)[0],
        'link': re.findall('<link>(.+?)</link>', article)[0],
        'date_published': re.findall('<pubDate>(.+?)</pubDate>', article)[0],
        'description': re.findall('<description>(.+?)</description>', article)[0].replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&nbsp;', ''),
        'source': re.findall('<source .+?>(.+?)</source>', article)[0],
    }


def get_news(ticker, n):
    headers = {
        'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}

    url = f'https://news.google.com/rss/search?q={ticker}&hl=en-US&gl=US&ceid=US:en&num={n}'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    data = response.content.decode('utf-8')
    data = re.findall('<item>(.+?)</item>', data)
    data = [clean_article(article) for article in data]

    return data

print(get_news('aapl', 5))
