from django.db import models


class LargestTown(models.Model):
    town = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    population = models.FloatField()

    def __str__(self):
        return 'town: {},country:{}'.format(self.town, self.country)


class Demography(models.Model):
    continents = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    population = models.FloatField()
    area = models.FloatField()
    density = models.FloatField()
    birthRate = models.FloatField()
    deathRate = models.FloatField()
    lifeExpectancy = models.FloatField()
    infantMortality = models.FloatField()
    idh = models.FloatField()

    def __str__(self):
        return 'Pays:{}, Population:{}'.format(self.pays, self.population)
