from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from worldnation.models import Nations
from worldnations_api.serializers import NationsSerializer


# Create your views here.
class NationsAPIViewSet(ModelViewSet):
    queryset = Nations.objects.all()
    serializer_class = NationsSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('nation', 'country', )
