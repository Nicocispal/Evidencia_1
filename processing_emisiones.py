import pandas as pd
import numpy as np 
import seaborn as sns 
from universal_functions import *


def process_emisiones():
    sio_file_emision= 'downloads/Emision.csv'
    df_emision= pd.read_csv(sio_file_emision, encoding = 'utf8', sep = ',', on_bad_lines='warn')
    pd.options.display.float_format = '{:.2f}'.format
    df_emision = df_emision.drop('CLAVE_INS', axis=1)
    print(df_emision.info())

    df_emision['EDAD'] = df_emision['EDAD'].replace('No disponible ', -1)

    df_emision.loc[df_emision['EDAD'] == -1]

    df_emision['MONEDA'] = df_emision['MONEDA'].replace('No disponible ', 'Varias monedas')

    df_emision.loc[df_emision['MONEDA'] == 'Varias monedas']
    unique_values(df_emision)
    df_emision['EDAD'].unique()
    print(df_emision.isnull().sum())

    object_columns = ['EDAD']

    for column in object_columns:
        print(column)
        if df_emision[column].dtype == 'object': 
                df_emision[column] = df_emision[column].astype(int)

    object_columns = ['NUMERO DE ASEGURADOS','PRIMA EMITIDA','SUMA ASEGURADA']

    for column in object_columns:
        if df_emision[column].dtype == 'object': 
            df_emision[column] = df_emision[column].str.replace(',', '').astype(int)

    print(df_emision.info())

    print(df_emision.columns)
    return df_emision
df_emision = process_emisiones()
print(df_emision.info())


