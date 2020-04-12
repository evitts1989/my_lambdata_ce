# my_lambdata/my_mod.py
             
import pandas as pd        
import numpy as np
import datetime as dt                      
    
def month_creator(dataframe, column):
    df = dataframe.copy()
    dataframe[column] = pd.to_datetime(dataframe[column], infer_datetime_format=True)
    dataframe['month'] = dataframe[column].dt.month
    return dataframe

def year_creator(dataframe, column):
    df = dataframe.copy()
    dataframe[column] = pd.to_datetime(dataframe[column], infer_datetime_format=True)
    dataframe['year'] = dataframe[column].dt.year
    return dataframe