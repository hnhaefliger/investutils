from rest_framework import serializers

from .models import Ticker
from .yfinance import get_ticker
from .robinhood import on_robinhood


class TickerSerializer(serializers.Serializer):
    '''
    Serializer for the ticker class.
    '''
    ticker = serializers.CharField()

    def create(self, validated_data):
        return Ticker.objects.create(
            ticker=validated_data['ticker'],
            ticker_type=validated_data['ticker_type'],
            on_robinhood=validated_data['on_robinhood'],
        )

    def validate(self, data):
        data['ticker'] = data['ticker'].upper()

        ticker_data = get_ticker(data['ticker'])

        if ticker_data['quoteResponse']['result']:
            data['ticker_type'] = ticker_data['quoteResponse']['result'][0]['quoteType'].upper()

        else:
            raise ValueError('Invalid ticker')

        data['on_robinhood'] = on_robinhood(data['ticker'], data['ticker_type'])

        return data

