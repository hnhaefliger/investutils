from rest_framework import routers
from .views import TickerViewSet

router = routers.DefaultRouter()

router.register('ticker', TickerViewSet, basename='ticker')

urlpatterns = router.urls
