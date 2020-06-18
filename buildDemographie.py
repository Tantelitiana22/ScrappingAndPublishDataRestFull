import pandas as pd
import csv

df_pop = pd.read_csv("dataCleaned/population_.csv")
df_idh = pd.read_csv("dataCleaned/idh_.csv")
df_mo = pd.read_csv("dataCleaned/mortalite_.csv")
df_nat = pd.read_csv("dataCleaned/natalite_.csv")
df_mo_inf = pd.read_csv("dataCleaned/mortalite-infantile_.csv")
df_esp_vie = pd.read_csv("dataCleaned/esperance-de-vie_.csv")

df1 = pd.merge(df_pop, df_idh, on="Pays", how='inner')
df2 = pd.merge(df1, df_mo, on="Pays", how='inner')
df3 = pd.merge(df2, df_nat, on="Pays", how='inner', suffixes=('_mortalite', '_ntatalite'))
df4 = pd.merge(df3, df_mo_inf, on="Pays", how='inner', suffixes=('', '_infan'))
df5 = pd.merge(df4, df_esp_vie, on="Pays", how='inner', suffixes=('', '_espVie'))
df_final = df5.drop(["Continent_x", 'Continent_y', 'Continent_infan', 'Continent_espVie'], axis=1)
df_final.to_csv("dataCleaned/Demography.csv", index=False)

