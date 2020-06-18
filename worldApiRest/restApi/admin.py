from django.contrib import admin
from .models import Demography, LargestTown


@admin.register(Demography)
class DemographyAdmin(admin.ModelAdmin):
    exclude = ['infantMortality']


@admin.register(LargestTown)
class LargestTownAdmin(admin.ModelAdmin):
    fields = ['town', 'country', 'population']
