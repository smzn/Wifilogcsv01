'''
Created on Aug 4, 2020

@author: haruka
'''
#This program
#Macアドレスが1つ以上あるデータのみにする

import wifilogcsv01.Wifilogcsv01_lib as mdl
import pandas as pd

#csv繝輔ぃ繧､繝ｫ縺ｮ蜿悶ｊ霎ｼ縺ｿ
def getCSV(file):
    return pd.read_csv(file, engine='python')

#df_data = getCSV('./csv/test.csv')
df_data = getCSV('./csv/test.csv')

df_data = df_data[df_data['AP'] != "NA"]#NAとるプログラム
wlib = mdl.Wifilogcsv01_lib(df_data) # 1つ以上データがあるものを返す
uniq_data = wlib.getuniqclient()
print(uniq_data)
path = './csv/test_uniq.csv'
wlib.saveuniqclient(path) # 1つ以上データがあるものをcsv保存する

uniq_data = wlib.getuniqclientsort()# 1つ以上データがあるものをソートして返す
print(uniq_data)
