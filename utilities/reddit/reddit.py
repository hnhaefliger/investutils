import random
import requests
import warnings
import time
import json


def clean_post(post):
    return {
        'subreddit': post['subreddit'],
        'selftext': post['selftext'],
        'title': post['title'],
        'downs': post['downs'],
        'name': post['name'],
        'ups': post['ups'],
        'total_awards_received': post['total_awards_received'],
        'link_flair_text': post['link_flair_text'],
        'score': post['score'],
        'created': post['created'],
        'author': post['author'],
        'created_utc': post['created_utc'],
        'id': post['id'],
        'subreddit_subscribers': post['subreddit_subscribers'],
    }


def get_posts(subreddit, after='', last_hrs=24*60*60):
    limit = 5
    t = time.time()
    posts = []

    while True:
        headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
        url = f'https://www.reddit.com/r/{subreddit}/new/.json?limit={limit}&after={after}'

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            response = requests.get(url, headers=headers, verify=False)

        data = response.json()['data']['children']
        data = [post['data'] for post in data if t - post['data']['created_utc'] < last_hrs]
        posts += data

        after = posts[-1]['name']
        
        if len(data) < limit:
            break

    return [clean_post(post) for post in posts]


def clean_comment(comment):
    return {
        'subreddit': comment['subreddit'],
        'selftext': comment['body'],
        'title': '',
        'downs': comment['downs'],
        'name': comment['name'],
        'ups': comment['ups'],
        'total_awards_received': comment['total_awards_received'],
        'link_flair_text': '',
        'score': comment['score'],
        'created': comment['created'],
        'author': comment['author'],
        'created_utc': comment['created_utc'],
        'id': comment['id'],
    }


def get_comments(post):
    headers = {'User-Agent': ''.join([str(random.randint(0, 9)) for i in range(10)])}
    url = f'https://www.reddit.com/r/{post["subreddit"]}/comments/{post["id"]}/.json?'

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(url, headers=headers, verify=False)

    comments = response.json()[1]['data']['children']
    comments = [comment['data'] for comment in comments]

    comments = [clean_comment(comment) for comment in comments]

    return comments


def scrape_reddit(reddit):
    posts = get_posts(reddit)
    comments = [get_comments(post) for post in posts]

    return posts, comments


posts, comments = scrape_reddit('stocks')

print(posts[0], comments[0])
