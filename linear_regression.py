import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as go
from universal_functions import *
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


sio_file_comisiones= 'downloads/Ors_entidad.csv'
df = pd.read_csv(sio_file_comisiones, encoding = 'utf8', sep = ',', on_bad_lines='warn')
pd.options.display.float_format = '{:.2f}'.format

df = df.replace(',', '', regex=True)

# Convertir las columnas a tipo int
columns_to_convert = ['NUMERO DE POLIZAS VIGENTES', 'RIESGOS ASEGURAADOS', 'RIESGOS ASEGURADOS VIGENTES',
                      'NUMERO DE SINIESTROS / RECLAMACIONES', 'PRIMA EMITIDA', 'COMISION DIRECTA',
                      'SUMA ASEGURADA', 'MONTO DE SINIESTRALIDAD', 'MONTO DE VENCIMIENTOS',
                      'MONTO DE RESCATE', 'AJUSTE DE GASTOS', 'MONTO DE DIVIDENDOS',
                      'MONTO DE SALVAMENTO', 'MONTO RECUPERADO']

df[columns_to_convert] = df[columns_to_convert].astype(int)

#Explicación a pandas de como interpretar las fechas
df['FECHA DE CORTE'] = pd.to_datetime(df['FECHA DE CORTE'], format='%d/%m/%Y')


df = df[df['PRIMA EMITIDA'] > 0]

#22 VALORES ÚNICOS, ES DECIR 22 MESES
print(df['FECHA DE CORTE'].nunique())
print(df['FECHA DE CORTE'].min()) 
print(df['FECHA DE CORTE'].max())

df = df.sort_values('FECHA DE CORTE')

fig = px.scatter(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
fig.show()

df['PRIMA ACUMULADA'] = df['PRIMA EMITIDA'].cumsum()
fig = px.line(df, x='FECHA DE CORTE', y='PRIMA ACUMULADA')
fig.show()


df = df.sort_values('FECHA DE CORTE')
df1 = df.groupby("FECHA DE CORTE")[['PRIMA EMITIDA', 'COMISION DIRECTA', 'MONTO DE SINIESTRALIDAD', 'NUMERO DE SINIESTROS / RECLAMACIONES',]].sum().reset_index()
fig = px.line(df1, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
fig.show()
# df1.to_csv('TEST.csv', index=False)


sio_file_comisiones= 'downloads/TEST.csv'
df = pd.read_csv(sio_file_comisiones, encoding = 'utf8', sep = ',', on_bad_lines='warn')
pd.options.display.float_format = '{:.2f}'.format
df['FECHA DE CORTE'] = pd.to_datetime(df['FECHA DE CORTE'])


fig = px.line(df, x= 'FECHA DE CORTE', y='PRIMA EMITIDA')
fig.show()
#No existe temporalidad ni es ciclico en la última edición del código.

#Para la regresión lineal múltiple nosotros decidimos filtrarlo de esta manera, ya que consideramos son las variables
#que explican de mejor manera el comportamiento de la base de datos.
X = df[['FECHA DE CORTE', 'COMISION DIRECTA', 'MONTO DE SINIESTRALIDAD','NUMERO DE SINIESTROS / RECLAMACIONES' ]]
y = df['PRIMA EMITIDA']


categorical_features = ['FECHA DE CORTE']
one_hot = OneHotEncoder()
transformer = ColumnTransformer([('one_hot', one_hot, categorical_features)], remainder='passthrough')
transformed_X = transformer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(transformed_X, y, test_size=0.25, random_state=2509)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
score = regressor.score(X_test, y_test)
print("Coeficiente de determinación (R^2):", score)
y_pred = regressor.predict(X_test)
results = pd.DataFrame({'y_pred': y_pred, 'y_test': y_test})
print(results.head())

plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, color='blue', label='Valores reales')
plt.scatter(range(len(y_test)), y_pred, color='red', label='Predicciones')
plt.xlabel('Instancias')
plt.ylabel('PRIMA EMITIDA')
plt.title('Valores reales vs Predicciones')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(range(len(y_test)), y_test - y_pred, color='green')
plt.xlabel('Instancias')
plt.ylabel('Diferencia')
plt.title('Diferencia entre Valores reales y Predicciones')
plt.show()


fig = px.scatter(df, x=range(len(y_test)), y=y_test, color_discrete_sequence=['blue'], labels={'x': 'Instancias', 'y': 'PRIMA EMITIDA'}, title='Valores reales')
fig.add_trace(px.scatter(df, x=range(len(y_test)), y=y_pred, color_discrete_sequence=['red'], labels={'x': 'Instancias', 'y': 'PRIMA EMITIDA'}, title='Predicciones'))
fig.show()


diff = y_test - y_pred
fig = px.line(df, x=range(len(y_test)), y=diff, color_discrete_sequence=['green'], labels={'x': 'Instancias', 'y': 'Diferencia'}, title='Diferencia entre Valores reales y Predicciones')
fig.show()