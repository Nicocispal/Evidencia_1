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

def coma_remover(data):
    if type(data) == str:
        if "," in data:
            return int(data.replace(',',''))
    return int(data)