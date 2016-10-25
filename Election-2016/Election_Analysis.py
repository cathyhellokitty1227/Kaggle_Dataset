import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read datasets
demo = pd.read_csv('county_facts.csv')
results = pd.read_csv('primary_results.csv')

#Prelimary analysis on primary results
merge_var = ['state_abbreviation','fips']
Data = pd.merge(demo,results,left_on =merge_var,right_on=merge_var,how='inner' )
Data.dropna()

#Print first 10 records from data 
print(Data.head())

print('Full data has {} observation'.format(Data.shape[0]))

print('Full data has {} columns'.format(Data.shape[1]))


