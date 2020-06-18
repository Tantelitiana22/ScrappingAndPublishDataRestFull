import csv

import pandas as pd

from restApi.models import Demography, LargestTown

pathDemo = "../dataCleaned/Demography.csv"
pathTown = "../dataCleaned/villes_.csv"
df_demo = pd.read_csv(pathDemo)
df_town = pd.read_csv(pathTown)
colDemo = list(df_demo.columns)
colTown = list(df_town.columns)

with open(pathDemo) as csvfile:
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
    reader = csv.DictReader(csvFile)
    for row in reader:
        p = LargestTown(town=row["Ville"],
                        country=row["Pays"],
                        population=row[colTown[2]])
        p.save()
