from .serializers import TickerSerializer
from .models import Ticker
from .listings import get_all_listed

def update_tickers():
    for listing in get_all_listed():
        try:
            ticker = Ticker.objects.get(ticker=listing)
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