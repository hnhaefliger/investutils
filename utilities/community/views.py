from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .reddit import scrape_reddit
from .yfinance import get_trending, get_related
from .stocktwits import get_comments, get_top_watched, get_watchlist_count
from . import google


class RedditPostsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'subreddit'

    def get(self, request, *args, **kwargs):
        return Response(data='', status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        after, last = '', 24*60*60

        if 'after' in request.GET:
            after = request.GET['after']

        if 'last' in request.GET:
            last = request.GET['last']

        posts, comments = scrape_reddit(kwargs['subreddit'], after=after, last=last)

        for post in comments:
            posts += post

        return Response(data=posts, status=status.HTTP_200_OK)


class StocktwitsWatchlistViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def get(self, request, *args, **kwargs):
        return Response(data=get_top_watched(), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(data={'count': get_watchlist_count(kwargs['ticker'])}, status=status.HTTP_200_OK)


class YFinanceTrendingViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def get(self, request, *args, **kwargs):
        n = 5

        if 'count' in request.GET:
            n = request.GET['count']

        return Response(data=get_trending(n), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        n = 5

        if 'count' in request.GET:
            n = request.GET['count']

        return Response(data=get_related(n, kwargs['ticker']), status=status.HTTP_200_OK)


class StocktwitsCommentViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def retrieve(self, request, *args, **kwargs):
        n = 20

        if 'count' in request.GET:
            n = request.GET['count']

        return Response(data=get_comments(kwargs['ticker'], n), status=status.HTTP_200_OK)


class GoogleNewsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def retrieve(self, request, *args, **kwargs):
        return Response(data=google.get_news(kwargs['ticker'], n), status=status.HTTP_200_OK)
