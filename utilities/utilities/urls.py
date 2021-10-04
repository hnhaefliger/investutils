from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework import status

def empty(request):
    return Response(status=status.HTTP_200_OK)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),
    path('wakemydyno.txt', empty)
]
