from rest_framework import serializers
from .models import LargestTown, Demography


class LargestTownSerealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LargestTown
        fields = '__all__'


class DemographySerealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demography
        fields = '__all__'
