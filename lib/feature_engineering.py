import pandas as pd

channelsToDelete = [
    'Q_B_2_0_2','Q_B_2_0_3','Q_B_2_0_4','Q_B_2_0_6',
    'Q_B_2_0_7','Q_B_2_0_8','Q_B_2_0_9',
    'Q_G_3_0_2','Q_G_3_0_3','Q_G_3_0_4','Q_G_3_0_6',
    'Q_G_3_0_7','Q_G_3_0_8','Q_G_3_0_9',
    'Q_R_4_0_2','Q_R_4_0_3','Q_R_4_0_4','Q_R_4_0_6',
    'Q_R_4_0_7','Q_R_4_0_8','Q_R_4_0_9',
    'Q_NIR_8_0_2','Q_NIR_8_0_3','Q_NIR_8_0_4','Q_NIR_8_0_6',
    'Q_NIR_8_0_7','Q_NIR_8_0_8','Q_NIR_8_0_9',
    ]
# 28 dimensiones


'''def sumSatChannels(X, R=True, G=True, B=True, NIR=True):
    if R : X['Sum_R']=X.iloc[:,3:14].sum(axis=1).round().astype('int32')
    if G : X['Sum_G']=X.iloc[:,15:26].sum(axis=1).round().astype('int32')
    if B : X['Sum_B']=X.iloc[:,27:38].sum(axis=1).round().astype('int32')
    if NIR : X['Sum_NIR']=X.iloc[:,39:50].sum(axis=1).round().astype('int32')
    X.iloc[:,3:50] = X.iloc[:,3:50].round().astype('int32')
    return X
'''

def deleteRedundantChannels(X):
    X.drop(channelsToDelete,inplace=True,axis=1)
    return X