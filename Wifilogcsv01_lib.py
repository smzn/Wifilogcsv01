'''
Created on Aug 5, 2020

@author: haruka
'''
import pandas as pd

class Wifilogcsv01_lib :

    def __init__(self, df_data):
        self.df_data = df_data
        self.uniq_data = 0

    def getuniqclient(self):
        grouping = self.df_data.groupby('client')
        grouping_size = grouping.size()
        l_columns = list(grouping_size[grouping_size > 1].index)
        self.uniq_data = self.df_data[self.df_data['client'].isin(l_columns)]
        return self.uniq_data

    def saveuniqclient(self, path):
        self.uniq_data.to_csv(path, index=False)
        return 0

    def getuniqclientsort(self):
        return self.uniq_data.sort_values(by=['client','timestamp'])