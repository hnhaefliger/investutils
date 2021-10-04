from django.contrib import admin
from django.urls import path, include
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class EmptyViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'ticker'

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),
    path('wakemydyno.txt', EmptyViewSet)
]
