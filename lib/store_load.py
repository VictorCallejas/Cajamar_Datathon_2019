import pandas as pd

#READ
def readRAW(path):
    Xy_train = pd.read_csv(path + 'Modelar_UH2020.txt', sep="|", header=0)
    X_test = pd.read_csv(path + 'Estimar_UH2020.txt', sep="|", header=0)
    return Xy_train, X_test

def readHDF(path, estimar=False):
    if not estimar:
        X = pd.read_hdf(path,key='X_train')
        y = pd.read_hdf(path,key='y_train')
        return X, y
    
    X_test = pd.read_hdf(path,key='X_test')
    return X_test


#STORE
def storeCSV(path, X_train=None,y_train=None, X_test=None):
    if X_train is not None : X_train.to_csv(path+'X_train.csv',index = False, header=True)
    if y_train is not None : y_train.to_csv(path+'y_train.csv',index = False, header=True)
    if X_test is not None : X_test.to_csv(path+'X_test.csv',index = False, header=True)
    
def storeHDF(path, X_train=None, y_train=None, X_test=None, y_test=None):
    if X_train is not None : X_train.to_hdf(path,index = False, key='X_train',format='t')
    if y_train is not None : y_train.to_hdf(path,index = False, key='y_train',format='t')
    if X_test is not None : X_test.to_hdf(path,index = False, key='X_test',format='t')
    if y_test is not None : y_test.to_hdf(path,index = False, key='y_test',format='t')
