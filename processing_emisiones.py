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

def process_emisiones():
    """
    Carga del dataset al ambiente.
    """
    sio_file_emision= 'downloads/Emision.csv'
    df_emision= pd.read_csv(sio_file_emision, encoding = 'utf8', sep = ',', on_bad_lines='warn')
    pd.options.display.float_format = '{:.2f}'.format

    """
    Quitamos la columna 'CLAVE_INS' ya que desconocemos el significado de las mismas y para efectos estadísticos es irrelevante.
    """
    df_emision = df_emision.drop('CLAVE_INS', axis=1)

    """
    Al utilizar la función unique encontramos que 'EDAD' tiene valores que aparecen como 'No Disponible ', por lo que procedemos
    a cambiarlos por -1. Además en 'Moneda' se observaban valores como 'No Disponible ' por lo que procedimos a cambiarlo por 
    'Varias monedas'. Con la función loc buscamos que el cambiuo se haya efectuado.
    """
    unique_values(df_emision)
    df_emision['EDAD'].unique()
    df_emision['MONEDA'].unique()
    df_emision['EDAD'] = df_emision['EDAD'].replace('No disponible ', -1)
    df_emision.loc[df_emision['EDAD'] == -1]
    df_emision['MONEDA'] = df_emision['MONEDA'].replace('No disponible ', 'Varias monedas')
    df_emision.loc[df_emision['MONEDA'] == 'Varias monedas']

    """
    Revisamos si existen valores NaN, que para este dataset, no es el caso.
    """
    print(df_emision.isnull().sum())

    """
    Observamos las variables númericas y con la función for lo cambiamos a int, sin embargo para la columna 'EDAD' hicimos un 
    bucle aparte ya que no es necesario quitarle las comas.
    """

    print(df_emision.info())
    object_columns = ['EDAD']
    for column in object_columns:
        print(column)
        if df_emision[column].dtype == 'object': 
                df_emision[column] = df_emision[column].astype(int)

    """
    Aquí procedemos a hacer lo mismo pero con la transformación de las comas.
    """
    object_columns = ['NUMERO DE ASEGURADOS','PRIMA EMITIDA','SUMA ASEGURADA']
    for column in object_columns:
        if df_emision[column].dtype == 'object': 
            df_emision[column] = df_emision[column].str.replace(',', '').astype(int)
    return df_emision

"""
Con estas validaciones la data ya está en condiciones de ser analizada.
"""



