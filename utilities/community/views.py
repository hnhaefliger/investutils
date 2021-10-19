from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from . import reddit
from . import yfinance
from . import stocktwits
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

        posts, comments = reddit.scrape_reddit(kwargs['subreddit'], after=after, last=last)

        for post in comments:
            posts += post

        return Response(data=posts, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class YFinanceTrendingViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def get(self, request, *args, **kwargs):
        n = 5

        if 'count' in request.GET:
            n = request.GET['count']

        return Response(data=yfinance.get_trending(n), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        n = 5

        if 'count' in request.GET:
            n = request.GET['count']

        return Response(data=yfinance.get_related(n, kwargs['ticker']), status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class StocktwitsWatchlistViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def get(self, request, *args, **kwargs):
        return Response(data=stocktwits.get_top_watched(), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(data={'count': stocktwits.get_watchlist_count(kwargs['ticker'])}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class StocktwitsCommentViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def retrieve(self, request, *args, **kwargs):
        n = 20

        if 'count' in request.GET:
            n = request.GET['count']

        return Response(data=stocktwits.get_comments(kwargs['ticker'], n), status=status.HTTP_200_OK)


class StocktwitsSentimentViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def retrieve(self, request, *args, **kwargs):
        return Response(data=stocktwits.get_sentiment(kwargs['ticker']), status=status.HTTP_200_OK)


class StocktwitsMessageVolumeViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def retrieve(self, request, *args, **kwargs):
        return Response(data=stocktwits.get_message_volume(kwargs['ticker']), status=status.HTTP_200_OK)


class GoogleNewsViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def retrieve(self, request, *args, **kwargs):
        timedelta = 7

        if 'timedelta' in request.GET:
            try:
                timedelta = int(request.GET['timedelta'])

            except:
                return Response(data={'error': 'invalid timedelta value'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=google.get_news(kwargs['ticker'], timedelta=timedelta), status=status.HTTP_200_OK)
