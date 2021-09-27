from .serializers import TickerSerializer
from .models import Ticker
from .listings import get_all_listed
from .robinhood import on_robinhood
from .yfinance import get_ticker

def update_tickers():
    for listing in get_all_listed():
        try:
            ticker = Ticker.objects.get(ticker=listing)
            
            result = get_ticker(ticker.ticker)['quoteResponse']['result']

            if result:
                if result[0]['quoteType'].upper() == ticker.ticker_type:
                    ticker.on_robinhood = on_robinhood(ticker.ticker, ticker.ticker_type)

                else:
                    ticker.delete()

            else:
                ticker.delete()

        except: pass

        serializer = TickerSerializer(data={
            'ticker': listing,
        })

        try:
            serializer.is_valid()
            serializer.save()

        except: pass

    return True
