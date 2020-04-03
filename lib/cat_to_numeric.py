import pandas as pd

cadastral_replace_map = {'1': 9, '2': 8, '3': 7, '4': 6,'5':5,'6':4,'7':3,'8':2,'9':1,'C':11,'B':13,'A':15}

y_replace_map = {'RESIDENTIAL':1,'INDUSTRIAL':2,'PUBLIC':3,'RETAIL':4,'OFFICE':5,'OTHER':6,'AGRICULTURE':7}

def buildingFloorToNumeric(X, nan = 3):
    X.MAXBUILDINGFLOOR.fillna(nan, inplace=True)
    X.MAXBUILDINGFLOOR = X.MAXBUILDINGFLOOR.astype('int8')
    return X

def cadastralQualityToNumeric(X, nan = 4, replace_map = cadastral_replace_map):
    X.CADASTRALQUALITYID.replace(replace_map, inplace=True)
    X.CADASTRALQUALITYID.fillna(nan, inplace=True)
    X.CADASTRALQUALITYID = X.CADASTRALQUALITYID.astype('int8')
    return X

def yToNumeric(y, replace_map = y_replace_map):
    y = y.replace(replace_map).astype('int8')
    return y