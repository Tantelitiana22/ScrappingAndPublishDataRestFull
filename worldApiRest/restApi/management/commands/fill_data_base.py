from django.core.management.base import BaseCommand
from restApi.models import Demography, LargestTown
import pandas as pd
import csv
import os


class Command(BaseCommand):
    """Django command to load data from csv file to django database"""

    def handle(self, *args, **kwargs):
        self.stdout.write("load data from scv file to database...")
        pathDemo = "dataCleaned/Demography.csv"
        pathTown = "dataCleaned/villes_.csv"

        df_town = pd.read_csv(pathTown)
        colTown = list(df_town.columns)

        with open(pathDemo, 'r', encoding="utf-8") as csvfile:
            self.stdout.write("load Demography dataSet...")
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Demography(continents=row['Continent'],
                               pays=row['Pays'],
                               population=row['Population (hab.)'],
                               area=row['Superficie (km²)'],
                               density=row['Densité (hab./km²)'],
                               birthRate=row['Taux (‰)_ntatalite'],
                               deathRate=row['Taux (‰)_mortalite'],
                               lifeExpectancy=row['Âge (ans)'],
                               infantMortality=row['Taux (‰)'],
                               idh=row['IDH (0,496)']
                               )
                p.save()

        with open(pathTown, 'r', encoding='utf-8') as csvFile:
            self.stdout.write("load ville dataSet...")
            reader = csv.DictReader(csvFile)
            for row in reader:
                p = LargestTown(town=row["Ville"],
                                country=row["Pays"],
                                population=row[colTown[2]])
                p.save()

        self.stdout.write(self.style.SUCCESS('Database loaded successfully!'))
