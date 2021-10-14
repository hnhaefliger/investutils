from rest_framework import routers
from .views import RedditPostsViewSet

router = routers.DefaultRouter()

router.register('reddit/posts', RedditPostsViewSet, basename='reddit/posts')

urlpatterns = router.urls
