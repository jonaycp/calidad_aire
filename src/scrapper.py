import requests
from bs4 import BeautifulSoup as bs
import urllib3
import wget
import os
import time
import pandas as pd
import numpy as np
import datetime


class Scrapper:

    local_path = '/home/jonay/Projects/calidadAire/calidad_aire/Files/'
    index_file = local_path + 'file_index.csv'
    columns_set = ['PROVINCIA','MUNICIPIO','ESTACION','MAGNITUD','PUNTO_MUESTREO','ANO','MES',
              'D01','V01','D02','V02','D03','V03','D04','V04','D05','V05','D06','V06','D07',
              'V07','D08','V08','D09','V09','D10','V10','D11','V11','D12','V12','D13','V13',
              'D14','V14','D15','V15','D16','V16','D17','V17','D18','V18','D19','V19','D20',
              'V20','D21','V21','D22','V22','D23','V23','D24','V24','D25','V25','D26','V26',
              'D27','V27','D28','V28','D29','V29','D30','V30','D31','V31']

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
    
    #Load and concatenate all the data from csv files listed in index
    def get_data(self):
        new_content = []
        for archivo in self.index['NOMBRE']:
            temp = pd.read_csv(self.local_path + archivo, sep=";", header=0)
            new_content.append(temp)
        return pd.concat(new_content)
    
    #Some codes from label PUNTO_NUESTREO have change in the time, here is changed by the current ones
    def update_punto_muestreo(self,my_data):
        #The value of PUNTO_MUESTREO is a code like AAAAAAAAA_BB_CC where the point code is the A*, the B* is Magnitud and C* i have no idea
        my_data['PUNTO_MUESTREO'] = my_data['PUNTO_MUESTREO'].str.split('_', expand=True)[0]

        #Replacing old codes to new ones
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079003'], '28079035')
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079003'], '28079035')
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079005'], '28079039')
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079010'], '28079038')
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079013'], '28079040')
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079020'], '28079036')
        my_data['ESTACION'] = my_data['ESTACION'].replace(['28079086'], '28079060')
        return my_data
    
    #The columns DXX are valid only if VXX == V, taken that information we replace no valid values by NaN and remove the unnecesary VXX columns
    def clean_invalid(self,my_data):
        dropable = []
        for number in range(1,32):
            my_data.loc[my_data["V{:02d}".format(number)] == "N", "D{:02d}".format(number)] = np.nan
            dropable.append("V{:02d}".format(number))

        return my_data.drop(dropable, axis=1)

madrid = Scrapper()
my_data = madrid.get_data()
my_data = madrid.update_punto_muestreo(my_data)
my_data = madrid.clean_invalid(my_data)
print(my_data)