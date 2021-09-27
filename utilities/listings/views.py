from django.contrib.auth.hashers import make_password, check_password

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Ticker
from .serializers import TickerSerializer
from .data import get_ticker_data


class TickerViewSet(viewsets.ViewSet):
    '''
    Viewset for checking if a ticker exists.
    '''
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def get(self, request, *args, **kwargs):
        '''
        List tickers.
        '''
        if 'offset' in request.GET:
            offset = int(request.GET['offset'])

        else:
            offset = 0

        if 'limit' in request.GET:
            limit = int(request.GET['limit'])

        else:
            limit = 20

        query_set = Ticker.objects.all()

        if 'ticker_type' in request.GET:
            query_set = query_set.filter(ticker_type=request.GET['ticker_type'].upper())

        if 'on_robinhood' in request.GET:
            query_set = query_set.filter(on_robinhood=(request.GET['on_robinhood'].upper()=='TRUE'))

        data = [{
            'ticker': ticker.ticker,
            'ticker_type': ticker.ticker_type,
            'on_robinhood': ticker.on_robinhood,
        } for ticker in query_set[offset:offset+limit]]

        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        '''
        Get data about a ticker.
        '''
        
        try:
            data = Ticker.objects.get(ticker=kwargs['ticker'].upper())
            data = {
                'ticker': data.ticker,
                'ticker_type': data.ticker_type,
                'on_robinhood': data.on_robinhood,
            }
            data.update(get_ticker_data(data['ticker']))

            return Response(data=data, status=status.HTTP_200_OK)

        except:
            return Response(data={
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        '''
        Request to add a ticker.
        '''
        try:
            Ticker.objects.get(ticker=request.data['ticker'])

            return Response(data={
                'error': 'ticker is already in database',
            }, status=status.HTTP_400_BAD_REQUEST)

        except:
            serializer = TickerSerializer(data=request.data)

            if serializer.is_valid(raise_exception=False):
                data = serializer.save()
                data = {
                    'ticker': data.ticker,
                    'ticker_type': data.ticker_type,
                    'on_robinhood': data.on_robinhood,
                }
                data.update(get_ticker_data(data['ticker']))

                return Response(data=data, status=status.HTTP_200_OK)

            else:
                return Response(data={
                    'error': 'invalid data',
                }, status=status.HTTP_400_BAD_REQUEST)
