from rest_framework import routers
from .views import RedditViewSet

router = routers.DefaultRouter()

router.register('', RedditViewSet, basename='reddit')

urlpatterns = router.urls
