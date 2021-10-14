from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .reddit import scrape_reddit


class RedditViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'subreddit'

    def get(self, request, *args, **kwargs):
        return Response(data='', status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        after, last = '', 24*60*60

        if 'after' in request['GET']:
            after = request['GET']['after']

        if 'last' in request['GET']:
            last = request['GET']['last']

        posts, comments = scrape_reddit(kwargs['subredddit'], after=after, last=last)

        for post in comments:
            posts += post

        return Response(posts, status=status.HTTP_200_OK)

