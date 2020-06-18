import numpy as np
import pandas as pd
import re
import glob


def getColumnsStringType(dfEnt):
    dfFunc = dfEnt.copy()
    columns = list(dfFunc.columns)
    new_columns = []
    for col in columns:
        if bool(re.search('\d', dfFunc[col].iloc[0])):
            temp = (
                dfFunc[col].str.replace('\s+', '').
                apply(lambda x: '.'.join(re.findall('\d+', x)))
            )
            newName = str(col) + ' (' + dfFunc[col].iloc[0].split(' ')[-1] + ')'
            new_columns.append(newName)
            temp[temp == ''] = np.nan
            dfFunc[col] = temp.astype(float)
        else:
            new_columns.append(col)

    dfFunc.columns = new_columns
    return dfFunc


if __name__ == "__main__":

    list_data = glob.glob("data/*.csv")
    for file in list_data:
        if 'palmares_' in file:
            temp = file.split('/')[1]
            newFileName = temp.replace('palmares_', '')
        else:
            newFileName = "langues_le_plus_parlees.csv"

        readData = pd.read_csv(file)
        dataToSave = getColumnsStringType(readData)
        dataToSave.to_csv("dataCleaned/"+newFileName, index=False)