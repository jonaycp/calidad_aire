import pandas as pd

# Usar Pandas library para leer csv files y sacar graficas
class Graph_Module:
    my_dataset = pd.DataFrame()
    
    
    def __init__(self,dataset):
        self.my_dataset = dataset

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
