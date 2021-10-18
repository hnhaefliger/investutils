from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('reddit/posts', RedditPostsViewSet, basename='reddit/posts')
router.register('yfinance/trending', YFinanceTrendingViewSet, basename='yfinance/trending')
router.register('stocktwits/watchlist', StocktwitsWatchlistViewSet, basename='stocktwits/watchlist')
router.register('stocktwits/comments', StocktwitsCommentViewSet, basename='stocktwits/comments')
router.register('stocktwits/sentiment', StocktwitsSentimentViewSet, basename='stocktwits/sentiment')
router.register('stocktwits/message_volume', StocktwitsMessageVolumeViewSet, basename='stocktwits/message_volume')
router.register('google/news', GoogleNewsViewSet, basename='google/news')


urlpatterns = router.urls
