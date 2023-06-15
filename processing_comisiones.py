"""
Equipo 1 CSF
Nicolás Cisneros Palma - A01029883
Jorge Martínez Rodríguez - A01351346
Leonardo Chico Reyes - A01029882
"""
import pandas as pd
import numpy as np 
import seaborn as sns 
from universal_functions import *


"""
Esta primera parte del proyecto consistió en realizar ingeniera de datos, es decir, verificar por datos faltantes, filas repetidas,
tipo de valores, valores únicos y a partir de todo esto, enfocar los trabajos en resolver las situaciones que se puedan suscitar, 
con la finalidad de que a partir de los cambios resultantes en el df, podamos hacer un análisis descriptiva, clustering y para 
el caso del dataset ORS modelos de predicción.
"""



"""
Todo este proceso fue englobado en una función para poder invocarla en los demás archivos y no tener cientos de lineas repetitivas
en todos los archivos.
"""
def process_comissions_df():
    """
    Carga del dataset al ambiente.
    """
    sio_file_comisiones= 'downloads/Comisiones.csv'
    df_comisiones= pd.read_csv(sio_file_comisiones, encoding = 'utf8', sep = ',', on_bad_lines='warn')

    pd.options.display.float_format = '{:.2f}'.format
    """
    Verificar el tipo de valores que incluye el df.
    """
    print(df_comisiones.info())


    """
    Estas fueron las columnas que tienen números, sin embargo aparecen de clase objeto, por lo tanto utilizamos un for
    para convertirlas a tipo int y aquí mismo retirar las comas para que sea maniobrable la información.
    """

    print(df_comisiones.info())
    object_columns = ['NUMERO DE ASEGURADOS', 'PRIMA CEDIDA', 'COMISIONES DIRECTAS','FONDO DE INVERSIÓN','FONDO DE ADMINISTRACION','MONTO DE DIVIDENDOS','MONTO DE RESCATE']
    for column in object_columns:
        if df_comisiones[column].dtype == 'object': 
            df_comisiones[column] = df_comisiones[column].str.replace(',', '').astype(int)

    
    """
    Revisar valores únicos para verificar que no existan datos extraños o con signos no deseados.
    """
    print(unique_values(df_comisiones))

    """
    Revisar filas duplicadas con la función duplicated_rows que proviene del archivo 'universal_functions.py'
    """
    duplicated_rows(df_comisiones)

    """
    Revisar por datos NaN, que en este caso no tenemos.
    """
    print(df_comisiones.isnull().sum())

    """
    Utilizar la función 'describe' de pandas para ver que no existan estadísticas atípicas.
    """
    df_comisiones.describe()

    categorical1 = [var for var in df_comisiones.columns if df_comisiones[var].dtype=='O']
    print('There are {} categorical variables'.format(len(categorical1)))
    print('The categorical variables are:', categorical1)
    return df_comisiones

"""
Con estas validaciones la data ya está en condiciones de ser analizada.
"""