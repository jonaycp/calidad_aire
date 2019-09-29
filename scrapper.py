import requests
from bs4 import BeautifulSoup as bs
import urllib3
import wget
import os

head = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "X-Requested-With": "XMLHttpRequest"
}

url = "https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD"

req = requests.get(url, headers=head)
req.raise_for_status()  #throw exception if failure
soup = bs(req.text, 'html.parser')

#TODO generalize this to include any value inside class for links
fichero = soup.find_all(class_="asociada-link ico-csv")
#The following one is equivalent to previous
#fichero2=soup(class_="asociada-link ico-csv")

#Loop to iterate all items and download files with csv
#HACK the href are incomplete, it needs before the link https://datos.madrid.es
links = []
for i in fichero:
    links.append('https://datos.madrid.es'+i['href'])

len(links)
# To download csv files, that are test based, it is better to use wget
# Apparently requests lib downloads files in a binary format, and it is not
# clear to me how to transform that to text.
for elink in links:
    wget.download(elink, os.path.join('/home/victor/development/calidad_aire/', os.path.basename(elink)))

# THIS SHOULD BE ALL

#Now we have all in place to start downloading the files
# for elink in links:
#     res = requests.get(elink)
#     try:
#         res.raise_for_status()
#     except Exception as exc:
#         print('File ' + elink + ' failed with error %s' % (exc))
# 
#     #TODO save to a user defined path. for now is fixed
#     dataFile = open(os.path.join('~/development/calidad_aire/', os.path.basename(elink)), 'wb')
#     for chunk in res.iter_content(100000):
#         dataFile.write(chunk)
#     dataFile.close()
#Finishedfor elink in 
