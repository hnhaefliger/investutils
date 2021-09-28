from rest_framework import routers
from .views import TickerViewSet, ChartViewSet

router = routers.DefaultRouter()

router.register('ticker', TickerViewSet, basename='ticker')
router.register('chart', ChartViewSet, basename='chart')

urlpatterns = router.urls
