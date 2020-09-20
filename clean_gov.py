import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#retrieve data
df = pd.read_csv('data/gov_data.csv')
us_data = df[df.country_name == 'United States']
uk_data = df[df.country_name == 'United Kingdom']
jp_data = df[df.country_name == 'Japan']
print(us_data)

#start date check
us_min = us_data['date'].min()
uk_min = uk_data['date'].min()
jp_min = jp_data['date'].min()
start_date = max(us_min, uk_min, jp_min) #2020-01-01
print(start_date)

us_max = us_data['date'].max()
uk_max = uk_data['date'].max()
jp_max = jp_data['date'].max()
end_date = min(us_max, uk_max, jp_max)
print(end_date)
