import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

df = pd.read_csv('MetroSales.csv')
print(df.head())

df_cat = pd.DataFrame(df.groupby('CATEGORY').SALES.agg('sum'))
print(df_cat.head)
#print(type(df_cat))
filename = 'CategorySales_'+ datetime.now().strftime("%m%d%Y_%H%M%S")+'.csv'
df_cat.to_csv(filename)
print("Saved data to file : ", filename)
