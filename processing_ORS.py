import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from universal_functions import *


def data_processing():
    sio_file_ors = 'downloads/Ors_entidad.csv'
    df = pd.read_csv(sio_file_ors, encoding='utf8', sep=',', on_bad_lines='warn')
    pd.options.display.float_format = '{:.2f}'.format
    df = df.drop('CLAVE_INS', axis=1) 
    df = df.replace(',', '', regex=True)


    columns_to_convert = ['NUMERO DE POLIZAS VIGENTES', 'RIESGOS ASEGURAADOS', 'RIESGOS ASEGURADOS VIGENTES',
                        'NUMERO DE SINIESTROS / RECLAMACIONES', 'PRIMA EMITIDA', 'COMISION DIRECTA',
                        'SUMA ASEGURADA', 'MONTO DE SINIESTRALIDAD', 'MONTO DE VENCIMIENTOS',
                        'MONTO DE RESCATE', 'AJUSTE DE GASTOS', 'MONTO DE DIVIDENDOS',
                        'MONTO DE SALVAMENTO', 'MONTO RECUPERADO']

    df[columns_to_convert] = df[columns_to_convert].astype(int)


    df['FECHA DE CORTE'] = pd.to_datetime(df['FECHA DE CORTE'], format='%d/%m/%Y')


    df = df[df['PRIMA EMITIDA'] > 0]

    print(df.isna().sum())
    print(df.dtypes)
    print(duplicated_rows(df))


    print(df['FECHA DE CORTE'].nunique())
    print(df['FECHA DE CORTE'].min()) 
    print(df['FECHA DE CORTE'].max())

    df = df.sort_values('FECHA DE CORTE')
    return df

# def delimitation():
#     fig = px.scatter(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
#     fig.show()

#     df = df.sort_values('FECHA DE CORTE')
#     df = df.groupby("FECHA DE CORTE")[['COMISION DIRECTA','PRIMA EMITIDA', 'MONTO DE SINIESTRALIDAD']].sum().reset_index()
#     fig = px.line(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
#     fig.show()
#     df1 = df[['FECHA DE CORTE', 'PRIMA EMITIDA']]
#     df1['Diferencia'] = df1.groupby(df1['FECHA DE CORTE'].dt.year)['PRIMA EMITIDA'].diff().fillna(df1['PRIMA EMITIDA'])
#     df1 = df1.drop(df1.index[0])

#     fig = px.line(df1, x = 'FECHA DE CORTE', y='Diferencia')
#     fig.show()
#     fig = px.scatter(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
#     fig.show()


#     df = df.sort_values('FECHA DE CORTE')
#     df = df.groupby("FECHA DE CORTE")[['COMISION DIRECTA','PRIMA EMITIDA', 'MONTO DE SINIESTRALIDAD']].sum().reset_index()
#     fig = px.line(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
#     fig.show()
#     df1 = df[['FECHA DE CORTE', 'PRIMA EMITIDA']]
#     df1['Diferencia'] = df1.groupby(df1['FECHA DE CORTE'].dt.year)['PRIMA EMITIDA'].diff().fillna(df1['PRIMA EMITIDA'])
#     df1 = df1.drop(df1.index[0])

#     fig = px.line(df1, x = 'FECHA DE CORTE', y='Diferencia')
#     fig.show()
#     return df1


