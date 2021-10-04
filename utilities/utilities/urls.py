from django.contrib import admin
from django.urls import path, include
from rest_framework import status
from rest_framework.response import Response


def empty(request):
    return Response(data='asdf', status=status.HTTP_200_OK)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),
    path('wakemydyno.txt', empty)
]
