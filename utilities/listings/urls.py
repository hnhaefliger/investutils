from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('ticker', TickerViewSet, basename='ticker')
router.register('chart', ChartViewSet, basename='chart')
router.register('summary_detail', SummaryDetailViewSet, basename='summary_detail')
router.register('asset_profile', AssetProfileViewSet, basename='asset_profile')
router.register('financial_data', FinancialDataViewSet, basename='financial_data')
router.register('key_statistics', KeyStatisticsViewSet, basename='key_statistics')

urlpatterns = router.urls
