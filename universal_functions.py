"""
Equipo 1 CSF
Nicolás Cisneros Palma - A01029883
Jorge Martínez Rodríguez - A01351346
Leonardo Chico Reyes - A01029882
"""

"""
Este apartado es para tener funciones universales de validación de datos, se realizó este nuevo archivo .py para únicamente
tener que invocarlas en los demás archivos y no tener lineas de código innecesarias.
"""

"""
Función para revisar valores únicos de un df
"""
def unique_values(data_frame):
    dict_unique = {}
    for c in data_frame:
        values = data_frame[c].unique()
        dict_unique[c] = values

    return dict_unique

"""
Función para revisar columnas repetidas en un df
"""
def duplicated_rows(data_frame):
    dict_duplicates = {}
    rows = data_frame.duplicated(keep=False)
    duplicated_data = data_frame[rows]
    for i, row in duplicated_data.iterrows():
        dict_duplicates[i] = row.values.tolist()
    return dict_duplicates

"""
Función para remover las comas en un df.
"""
def coma_remover(data):
    if type(data) == str:
        if "," in data:
            return int(data.replace(',',''))
    return int(data)