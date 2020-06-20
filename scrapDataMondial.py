import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import os

if not os.path.isdir("data"):
    os.mkdir("data")

urlBase = "https://www.populationdata.net"
sizeUrlBase = len(urlBase)
content = requests.get("https://www.populationdata.net/palmares/ipe/").content
soup = BeautifulSoup(content, "html.parser")

menuPalmares = soup.find("ul", id="menu-palmares")
listHref = menuPalmares.findAll("a", href=True)
links_with_text = [a['href'][sizeUrlBase:] for a in listHref if a.text][1:]


def buildData(link):
    print("current link:", link)
    url = urlBase + link
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    tables = soup.findAll('table')
    if len(tables) > 1:
        table = tables[1]
    else:
        table = tables[0]
    header = [col.text for col in table.findAll('th')]
    if len(header) == 0:
        header = ['rang', 'Langues', 'Localisations (principales)', 'Nombre (millions, estimations 2006)']
    dataFileName = "data/" + link[1:].replace('/', '_') + ".csv"
    df = pd.DataFrame(columns=header[1:])
    df.to_csv(dataFileName, index=False)

    with open(dataFileName, 'a', encoding='utf-8') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=header[1:], lineterminator='\n')

        allRows = table.find('tbody')

        for r in allRows.findAll('tr'):
            row = []
            for td in r.findAll('td'):
                if td.find('a'):
                    row.append(td.find('a').text)
                elif td.find('div'):
                    row.append(td.find('div').text)
                else:
                    row.append(td.text)
            dico = dict(zip(header[1:], row[1:]))
            if len(dico) != 0 and 'Localisations (principales)' not in row:
                writer.writerow(dico)


if __name__ == "__main__":
    for l in links_with_text:
        buildData(l)
