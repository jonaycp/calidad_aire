import requests
from bs4 import BeautifulSoup as bs
import urllib3
import wget
import os
import time
import pandas as pd
import datetime


class Scrapper:

    local_path = '/home/jonay/Projects/calidadAire/calidad_aire/Files/'
    index_file = local_path + 'file_index.csv'

    head = {"User-Agent": "Mozilla/3.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "X-Requested-With": "XMLHttpRequest"
        }
    #url = "https://datos.madrid.es/portal/site/egob/menuitem.c03c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD"
    url = 'https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default'
    domain = 'https://datos.madrid.es'
    index = pd.DataFrame()
    columns = ['NOMBRE', 'TAMANO', 'FECHADESCARGA']


    #Check if we have the index file, otherwise it will be created empty
    def __init__(self):
        try:
            #If file doesn't exist it will throw an exception
            self.index = pd.read_csv(self.index_file, sep=";", header=None, names=self.columns)
        except:
            #Create an empty file
            df = pd.DataFrame()
            df.to_csv(self.index_file, mode='a', sep = ';', index=False, header=False)

    #Takes all filenames on the web, check if exist new ones and download and update in that case
    def update(self):
        req = requests.get(self.url, headers=self.head)
        req.raise_for_status()  #throw exception if failure
        soup = bs(req.text, 'html.parser')

        #TODO generalize this to include any value inside class for links
        fichero = soup.find_all(class_="asociada-link ico-csv")

        #Loop to iterate all items and download files with csv
        #HACK the href are incomplete, it needs before the link https://datos.madrid.es
        links = []
        for i in fichero:
            links.append(self.domain + i['href'])

        df_new_data = pd.DataFrame()
        new_lines_counter = 0

        for elink in links: 
            if (self.index.empty) or (os.path.basename(elink) not in list(self.index['NOMBRE'])):
                
                #Download the file
                wget.download(elink, os.path.join(self.local_path, os.path.basename(elink)))
                time.sleep(2)

                #Creation of the new row for the new file/s found
                new_row = {self.columns[0]: os.path.basename(elink),
                        self.columns[1] : os.stat(os.path.join(self.local_path, os.path.basename(elink))).st_size,
                        self.columns[2]: datetime.datetime.now()}

                #Adding the new rows
                df_new_data = df_new_data.append(new_row, ignore_index=True)
                new_lines_counter += 1
        
        #writting result in file
        df_new_data.to_csv(self.index_file, sep=";", mode='a', index=False, header=False)
        
        
        self.index = pd.read_csv(self.index_file,sep=";", header=None,names=self.columns)
        
        #Just for testing, change it to something more professional like using logging library
        if new_lines_counter == 0:
            print("No hay nuevos ficheros")
            return 0
        else:
            print(f"/nSe han descargado {new_lines_counter} nuevos archivos de datos")
            return new_lines_counter

    def get_data(self):
        new_content = []
        for archivo in self.index['NOMBRE']:
            new_content.append(pd.read_csv(self.local_path + archivo, sep=";", index_col=1))

        return pd.concat(new_content)

madrid = Scrapper()
print(madrid.index)
madrid.update()
print(madrid.get_data().head(20))