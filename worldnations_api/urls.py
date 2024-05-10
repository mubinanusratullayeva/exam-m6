from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import NationsAPIViewSet

routers = DefaultRouter()
routers.register("nations", viewset=NationsAPIViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
