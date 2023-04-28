from comisiones_processing import process_comissions_df
import pandas as pd
import numpy as np 
import seaborn as nb
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
#python3 Descriptive_statistics.py

df = process_comissions_df()

stats = df.describe(include='all')
print(stats)

cols1 = ['EDAD', 'NUMERO DE ASEGURADOS', 'PRIMA CEDIDA', 'COMISIONES DIRECTAS', 'FONDO DE INVERSIÓN', 'FONDO DE ADMINISTRACION', 'MONTO DE DIVIDENDOS', 'MONTO DE RESCATE']
cols = ['NUMERO DE ASEGURADOS', 'PRIMA CEDIDA', 'COMISIONES DIRECTAS', 'FONDO DE INVERSIÓN', 'FONDO DE ADMINISTRACION', 'MONTO DE DIVIDENDOS', 'MONTO DE RESCATE']

#Statistics
for col in cols1:
    print(f'Estadística descriptiva para la columna "{col}":')
    print(df[col].describe())
    print('\n')


#Outliers
for col in cols:
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.boxplot(df[col], vert=False)
    ax.set_title(col)
    plt.show()

#Kmeans
X = df[cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.labels_
for col in cols:
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(df['EDAD'], df[col], c=labels, cmap='rainbow')
    ax.set_xlabel('EDAD')
    ax.set_ylabel(col)
    ax.set_title(f'Clustering de {col} contra la Edad')
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.show()

