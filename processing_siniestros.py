import pandas as pd
import numpy as np 
import seaborn as sns 
from universal_functions import *

def process_siniestros():
    sio_file_siniestros = 'downloads/Siniestros.csv'
    sio_file_siniestros = 'downloads/Siniestros.csv'
    df_siniestro = pd.read_csv(sio_file_siniestros, encoding='utf8', sep=',', on_bad_lines='warn', low_memory=False)
    pd.options.display.float_format = '{:.2f}'.format
    df_siniestro = df_siniestro.drop('CLAVE_INS', axis=1)

    print(df_siniestro.info())

    df_siniestro['EDAD'] = df_siniestro['EDAD'].replace('No disponible ', -1)

    df_siniestro.loc[df_siniestro['EDAD'] == -1]

    unique_values(df_siniestro)

    df_siniestro['EDAD'].unique

    print(df_siniestro.isnull().sum())

    object_columns = ['EDAD']

    for column in object_columns:
        print(column)
        if df_siniestro[column].dtype == 'object': 
            df_siniestro[column] = df_siniestro[column].astype(int)

    df_siniestro['NUMERO DE SINIESTROS'] = df_siniestro['NUMERO DE SINIESTROS'].fillna(0)

    df_siniestro['NUMERO DE SINIESTROS'] = df_siniestro['NUMERO DE SINIESTROS'].apply(coma_remover)

    object_columns = ['MONTO RECLAMADO','VENCIMIENTOS','MONTO PAGADO','MONTO DE REASEGURO']

    for column in object_columns:
        print(column)
        if df_siniestro[column].dtype == 'object': 
            df_siniestro[column] = df_siniestro[column].str.replace(',', '').astype(int)
    return df_siniestro

df = process_siniestros()
print(df.info())

