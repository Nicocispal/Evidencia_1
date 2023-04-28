import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as go

def unique_values(data_frame):
    dict_unique = {}
    for c in data_frame:
        values = data_frame[c].unique()
        dict_unique[c] = values

    return dict_unique

def duplicated_rows(data_frame):
    dict_duplicates = {}
    rows = data_frame.duplicated(keep=False)
    duplicated_data = data_frame[rows]
    for i, row in duplicated_data.iterrows():
        dict_duplicates[i] = row.values.tolist()
    return dict_duplicates

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

    print(df_comisiones[categorical1].head())

    for var in categorical1:
        print(df_comisiones[var].value_counts())


    print(df_comisiones[categorical1].isnull().sum())

    df_comisiones = pd.get_dummies(df_comisiones, columns=['PLAN DE LA POLIZA', 'MODALIDAD DE LA POLIZA', 'MONEDA', 'ENTIDAD ', 'SEXO', 'FORMA DE VENTA', 'TIPO DIVIDENDO'])
    print(df_comisiones.head())

    return df_comisiones