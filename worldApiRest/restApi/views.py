from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DemographySerealizer, LargestTownSerealizer
from .models import Demography, LargestTown


class DemographyViewSet(viewsets.ModelViewSet):
    queryset = Demography.objects.all().order_by('population')
    serializer_class = DemographySerealizer


class LargestTownViewSet(viewsets.ModelViewSet):
    queryset = LargestTown.objects.all().order_by('population')
    serializer_class = LargestTownSerealizer

