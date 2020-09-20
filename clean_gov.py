import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#retrieve data
df = pd.read_csv('data/Covid_govt_data.csv')
us = df[df.country_name == 'United States']
uk = df[df.country_name == 'United Kingdom']
jp = df[df.country_name == 'Japan']

#remove workplace_closing
us = us.drop("workplace_closing", axis=1)
uk = uk.drop("workplace_closing", axis=1)
jp = jp.drop("workplace_closing", axis=1)

#remove row if NaN
us = us.dropna(axis=0)
uk = uk.dropna(axis=0)
jp = jp.dropna(axis=0)

#to csv
us.to_csv('data/us_gov.csv')
uk.to_csv('data/uk_gov.csv')
jp.to_csv('data/jp_gov.csv')

#start date check
us_min = us['date'].min()
uk_min = uk['date'].min()
jp_min = jp['date'].min()
start_date = max(us_min, uk_min, jp_min) #2020-01-01
print(start_date)
