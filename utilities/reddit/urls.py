from rest_framework import routers
from .views import RedditViewSet

router = routers.DefaultRouter()

router.register('posts', RedditViewSet, basename='posts')

urlpatterns = router.urls
