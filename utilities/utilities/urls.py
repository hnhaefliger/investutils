from django.contrib import admin
from django.urls import path, include
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def empty(request):
    return Response(data='asdf', status=status.HTTP_200_OK)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),
    path('wakemydyno.txt', empty)
]
