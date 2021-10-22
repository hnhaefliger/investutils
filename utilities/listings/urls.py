from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('ticker', TickerViewSet, basename='ticker')
router.register('chart', ChartViewSet, basename='chart')
router.register('summary_detail', SummaryDetailViewSet, basename='summary_detail')
router.register('asset_profile', AssetProfileViewSet, basename='asset_profile')
router.register('financial_data', FinancialDataViewSet, basename='financial_data')
router.register('key_statistics', KeyStatisticsViewSet, basename='key_statistics')
router.register('calendar_events', CalendarEventsViewSet, basename='calendar_events')
router.register('income_statement_quarterly', IncomeStatementQuarterlyViewSet, basename='income_statement_quarterly')
router.register('cashflow', CashflowStatementViewSet, basename='cashflow')
router.register('balancesheet', BalancesheetStatementViewSet, basename='balancesheet')
router.register('earnings', EarningsViewSet, basename='earnings')
router.register('esg', ESGViewSet, basename='esg')
router.register('price', PriceViewSet, basename='price')
router.register('type', TypeViewSet, basename='type')
router.register('insights', InsightsViewSet, basename='insights')

urlpatterns = router.urls
