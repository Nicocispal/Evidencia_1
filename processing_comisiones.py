import pandas as pd
import numpy as np 
import seaborn as sns 
from universal_functions import *


def process_comissions_df():
    sio_file_comisiones= 'downloads/Comisiones.csv'
    df_comisiones= pd.read_csv(sio_file_comisiones, encoding = 'utf8', sep = ',', on_bad_lines='warn')

    pd.options.display.float_format = '{:.2f}'.format

    object_columns = ['NUMERO DE ASEGURADOS', 'PRIMA CEDIDA', 'COMISIONES DIRECTAS','FONDO DE INVERSIÓN','FONDO DE ADMINISTRACION','MONTO DE DIVIDENDOS','MONTO DE RESCATE']

    for column in object_columns:
        if df_comisiones[column].dtype == 'object': 
            df_comisiones[column] = df_comisiones[column].str.replace(',', '').astype(int)

    print(df_comisiones.info())
    print(unique_values(df_comisiones))

    duplicated_rows(df_comisiones)

    print(df_comisiones.isnull().sum())
    print(df_comisiones.columns)

    df_comisiones.describe()

    categorical1 = [var for var in df_comisiones.columns if df_comisiones[var].dtype=='O']
    print('There are {} categorical variables'.format(len(categorical1)))
    print('The categorical variables are:', categorical1)
    return df_comisiones
