import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scrapper as sc

# Usar Pandas library para leer csv files y sacar graficas
class Data_Processing:
    my_dataset = pd.DataFrame()


    def __init__(self):
        self.my_dataset = sc.Extract().get_data()

    


    def get_punto_muestreo(self,punto_muestreo, magnitud=None, ano=None, mes=None, day=None):
        temp = self.my_dataset.loc[self.my_dataset['PUNTO_MUESTREO'] == punto_muestreo]

        #print(temp)        
        if magnitud is not None: 
            temp = temp.loc[temp['MAGNITUD'] == magnitud]
       # print(temp)
        if mes is not None: 
            temp = temp.loc[temp['MES'] == mes]
        
        if ano is not None: 
            temp = temp.loc[temp['ANO'] == ano]
        
        if day is not None:
            day_selected = "D{:02d}".format(day)
            temp = temp[['PROVINCIA', 'MUNICIPIO', 'ESTACION', 'MUNICIPIO', 'MAGNITUD', 'PUNTO_MUESTREO', 'ANO', 'MES', day_selected]]

        
        return temp
    
    #Input: original dataset
    #Output: original dataset with the day columns (D01, D02, D03...) replaced by a new column Total with the sum of all days
    def get_by_month(self):
        bymonth = self.my_dataset.loc[:,['PUNTO_MUESTREO','ANO', 'MES', 'MAGNITUD']]
        #List comprehension used to create a list of the column names for the days
        bymonth['TOTAL'] = self.my_dataset[[x + 1 for x in range(31)]].sum(axis=1,skipna=True) 
        return bymonth


##################################################################################################
#                                        TESTS                                                   #
##################################################################################################

hola = Data_Processing()
print(hola.my_dataset)
print(hola.get_by_month())