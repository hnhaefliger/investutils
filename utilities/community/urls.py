from rest_framework import routers
from .views import RedditPostsViewSet, YFinanceTrendingViewSet, StocktwitsWatchlistViewSet, StocktwitsCommentViewSet, GoogleNewsViewSet

router = routers.DefaultRouter()

router.register('reddit/posts', RedditPostsViewSet, basename='reddit/posts')
router.register('yfinance/trending', YFinanceTrendingViewSet, basename='yfinance/trending')
router.register('stocktwits/watchlist', StocktwitsWatchlistViewSet, basename='stocktwits/watchlist')
router.register('stocktwits/comments', StocktwitsCommentViewSet, basename='stocktwits/comments')
router.register('google/news', GoogleNewsViewSet, basename='google/news')


urlpatterns = router.urls
