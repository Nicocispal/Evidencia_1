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

def process_siniestros():
    """
    Carga del dataset al ambiente.
    """
    sio_file_siniestros = 'downloads/Siniestros.csv'
    sio_file_siniestros = 'downloads/Siniestros.csv'
    df_siniestro = pd.read_csv(sio_file_siniestros, encoding='utf8', sep=',', on_bad_lines='warn', low_memory=False)
    pd.options.display.float_format = '{:.2f}'.format

    """
    Quitamos la columna 'CLAVE_INS' ya que desconocemos el significado de las mismas y para efectos estadísticos es irrelevante.
    """
    df_siniestro = df_siniestro.drop('CLAVE_INS', axis=1)

    """
    Con la función unique encontramos los que en 'EDAD' hay valores como 'No Disponible ', por lo que procedemos a cambiarlo a -1
    para poder hacerlo int.
    """
    print(df_siniestro['EDAD'].unique)
    df_siniestro['EDAD'] = df_siniestro['EDAD'].replace('No disponible ', -1)
    df_siniestro.loc[df_siniestro['EDAD'] == -1]
    unique_values(df_siniestro)
    
    """
    Revisamos por valores NaN, que en este casi encontramos que en columna 'NUMERO DE SINIESTROS' existen, por lo que procedemos 
    a llenarlos con ceros.
    """
    print(df_siniestro.isnull().sum())
    df_siniestro['NUMERO DE SINIESTROS'] = df_siniestro['NUMERO DE SINIESTROS'].fillna(0)

    """
    Observamos las variables númericas y con la función for lo cambiamos a int, sin embargo para la columna 'EDAD' hicimos un 
    bucle aparte ya que no es necesario quitarle las comas.
    """
    object_columns = ['EDAD']
    for column in object_columns:
        print(column)
        if df_siniestro[column].dtype == 'object': 
            df_siniestro[column] = df_siniestro[column].astype(int)

  
    """
    Aquí procedemos a hacer lo mismo pero con la transformación de las comas.
    """
    df_siniestro['NUMERO DE SINIESTROS'] = df_siniestro['NUMERO DE SINIESTROS'].apply(coma_remover)
    object_columns = ['MONTO RECLAMADO','VENCIMIENTOS','MONTO PAGADO','MONTO DE REASEGURO']
    for column in object_columns:
        print(column)
        if df_siniestro[column].dtype == 'object': 
            df_siniestro[column] = df_siniestro[column].str.replace(',', '').astype(int)
    return df_siniestro
 
"""
Con estas validaciones la data ya está en condiciones de ser analizada.
"""

