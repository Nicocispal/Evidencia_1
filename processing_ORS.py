"""
Equipo 1 CSF
Nicolás Cisneros Palma - A01029883
Jorge Martínez Rodríguez - A01351346
Leonardo Chico Reyes - A01029882
"""
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
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


def data_processing():
    """
    Carga del dataset al ambiente.
    """
    sio_file_ors = 'downloads/Ors_entidad.csv'
    df = pd.read_csv(sio_file_ors, encoding='utf8', sep=',', on_bad_lines='warn')
    pd.options.display.float_format = '{:.2f}'.format

    """
    Quitamos la columna 'CLAVE_INS' ya que desconocemos el significado de las mismas y para efectos estadísticos es irrelevante.
    """
    df = df.drop('CLAVE_INS', axis=1) 

    """
    Con este método reemplazamos las comas por espacios para a posteriori poder hacer más transformaciones.
    """
    df = df.replace(',', '', regex=True)

    """
    Con la función integrada de pandas info, visualizamos las variables que son números pero a parecen como objeto, por lo que
    procedemos a hacer una lista para transfomarlas a int.
    """
    print(df.info())
    columns_to_convert = ['NUMERO DE POLIZAS VIGENTES', 'RIESGOS ASEGURAADOS', 'RIESGOS ASEGURADOS VIGENTES',
                        'NUMERO DE SINIESTROS / RECLAMACIONES', 'PRIMA EMITIDA', 'COMISION DIRECTA',
                        'SUMA ASEGURADA', 'MONTO DE SINIESTRALIDAD', 'MONTO DE VENCIMIENTOS',
                        'MONTO DE RESCATE', 'AJUSTE DE GASTOS', 'MONTO DE DIVIDENDOS',
                        'MONTO DE SALVAMENTO', 'MONTO RECUPERADO']

    df[columns_to_convert] = df[columns_to_convert].astype(int)


    """
     Convertimos 'FECHA DE CORTE' a datetime, además que le indicamos a pandas cual es el formato de nuestras fechas para que
     pueda hacer la conversión.
    """
    df['FECHA DE CORTE'] = pd.to_datetime(df['FECHA DE CORTE'], format='%d/%m/%Y')

    """
    Removemos los valores dentro de 'PRIMA EMITIDA' que son negativos, esto por indicación per se de la OSF.
    """
    df = df[df['PRIMA EMITIDA'] > 0]


    """
    Revisamos valores NaN, que en este caso n hay.
    """
    print(df.isna().sum())

    """
    Utilizamos la función duplicated_rows para revisar si existen filas duplicadas y no es el caso.
    """
    print(duplicated_rows(df))

    """
    Al final únicamente acomodamos el df por la columna 'FECHA DE CORTE'.
    """
    df = df.sort_values('FECHA DE CORTE')
    return df



def delimitation():
    df = data_processing()
    fig = px.scatter(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
    fig.show()

    df = df.sort_values('FECHA DE CORTE')
    df = df.groupby("FECHA DE CORTE")[['COMISION DIRECTA','PRIMA EMITIDA', 'MONTO DE SINIESTRALIDAD']].sum().reset_index()
    fig = px.line(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
    fig.show()
    df1 = df[['FECHA DE CORTE', 'PRIMA EMITIDA']]
    df1['Diferencia'] = df1.groupby(df1['FECHA DE CORTE'].dt.year)['PRIMA EMITIDA'].diff().fillna(df1['PRIMA EMITIDA'])
    df1 = df1.drop(df1.index[0])

    fig = px.line(df1, x = 'FECHA DE CORTE', y='Diferencia')
    fig.show()
    fig = px.scatter(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
    fig.show()


    df = df.sort_values('FECHA DE CORTE')
    df = df.groupby("FECHA DE CORTE")[['COMISION DIRECTA','PRIMA EMITIDA', 'MONTO DE SINIESTRALIDAD']].sum().reset_index()
    fig = px.line(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
    fig.show()
    df1 = df[['FECHA DE CORTE', 'PRIMA EMITIDA']]
    df1['Diferencia'] = df1.groupby(df1['FECHA DE CORTE'].dt.year)['PRIMA EMITIDA'].diff().fillna(df1['PRIMA EMITIDA'])
    df1 = df1.drop(df1.index[0])

    fig = px.line(df1, x = 'FECHA DE CORTE', y='Diferencia')
    fig.show()
    return df1


