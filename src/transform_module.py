
# This module transforms codes in data to readable references.
# Specific to this data, but with the idea to be generic.

# USE: for Pandas this will be used with .apply(transform). The apply is used 
# by a DataFrame choosing the column that we want to transform.
# TODO: make this generic and having more params that chose the dictionary to
# use in the transformation.
# CAVEAT: .apply uses the func as a lambda so we cannot decide the parameters
# passed. Maybe a fuction factories to create the new ones?

def transform (x, dict):
  # Create dictionary and compares against x to replace wiht text

  return dict.get(x, "Error en codigo de Medida.")

# Functions that determine the dictionary for the right column transformation.
def magnitud(x):

  magnitud = {1: "SO2", 6: "CO", 7: "NO", 8: "NO2", 9: "PM2.5", 10: "PM10", 
              12: "NOx", 14: "O3", 20: "TOL", 30: "BEN", 35: "EBE",
              37: "MXY", 38: "PXY", 39: "OXY", 42: "Total Hidrocarburos",
              43: "CH4", 44: "Hidrocarburos no metanicos"
            } 
  # return transform(x, magnitud)
  return magnitud.get(x, "Error en medida")

def estaciones(x):
  
  estacion = {
              '28079001': "P. Recoletos",           # Baja 2009
              '28079002': "Glta. de Carlos V",      # Baja 2006
              '28079035': "Pza. del Carmen",
              '28079004': "Pza. de España",
              '28079039': "Barrio del Pilar",
              '28079006': "Pza. Dr. Marañón",       # Baja 2009
              '28079007': "Pza. M. de Salamanca",   # Baja 2009
              '28079008': "Escuelas Aguirre",
              '28079009': "Pza. Luca de Tena",      # Baja 2009
              '28079038': "Cuatro Caminos",
              '28079011': "Av. Ramón y Cajal",
              '28079012': "Pza. Manuel Becerra",    # Baja 2009
              '28079040': "Vallecas",
              '28079014': "Pza. Fdez. Ladreda",     # Baja 2009
              '28079015': "Pza. Castilla",          # Baja 2008
              '28079016': "Arturo Soria",
              '28079017': "Villaverde Alto",
              '28079018': "C/ Farolillo",
              '28079019': "Huerta Castañeda",       # Baja 2009
              '28079036': "Moratalaz",
              '28079021': "Pza. Cristo Rey",        # Baja 2009
              '28079022': "Po. Pontones",           # Baja 2009
              '28079023': "Final C/ Alcalá",        # Baja 2009
              '28079024': "Casa de Campo",
              '28079025': "Santa Eugenia",          # Baja 2009
              '28079026': "Urb. Embajada (Barajas)",# Baja 2010
              '28079027': "Barajas",
              '28079047': "Méndez Álvaro",          # Alta 2009
              '28079048': "Po. Castellana",         # Alta 2010
              '28079049': "Retiro",                 # Alta 2010
              '28079050': "Pza. Castilla",          # Alta 2010
              '28079054': "Ensanche Vallecas",      # Alta 2009
              '28079055': "Urb. Embajada (Barajas)",# Alta 2010
              '28079056': "Plaza Elíptica",         # Alta 2010
              '28079057': "Sanchinarro",            # Alta 2009
              '28079058': "El Pardo",               # Alta 2009
              '28079059': "Parque Juan Carlos I",   # Alta 2009
              '28079060': "Tres Olivos",            # Alta 2010
              # Antiguos codigos de estaciones. Modificados en 2011
              '28079003': "Pza. del Carmen",
              '28079005': "Barrio del Pilar",
              '28079010': "Cuatro Caminos",
              '28079013': "Vallecas",
              '28079020': "Moratalaz",
              '28079086': "Tres Olivos"
  }

  # El dato de estacion viene con trailing que no nos vale. Solo cuenta el
  # primer bloque de numeros, asi que lo solucionamos aqui.
  x = x[:8]
  # DEBUG
  print(x)
  type(x)
  # return transform(x, estacion)
  return estacion.get(x, "No hay estacion para ese codigo")
