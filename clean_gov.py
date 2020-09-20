import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#retrieve data
df = pd.read_csv('data/Covid_govt_data.csv')
us_data = df[df.country_name == 'United States']
uk_data = df[df.country_name == 'United Kingdom']
jp_data = df[df.country_name == 'Japan']

#to csv
us_data.to_csv('data/us_gov.csv')
uk_data.to_csv('data/uk_gov.csv')
jp_data.to_csv('data/jp_gov.csv')

#start date check
us_min = us_data['date'].min()
uk_min = uk_data['date'].min()
jp_min = jp_data['date'].min()
start_date = max(us_min, uk_min, jp_min) #2020-01-01
print(start_date)
