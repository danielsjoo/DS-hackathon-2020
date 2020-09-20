import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#retrieve data
df = pd.read_csv('data/Covid_govt_data.csv')
us_data = df[df.country_name == 'United States']
uk_data = df[df.country_name == 'United Kingdom']
jp_data = df[df.country_name == 'Japan']

#start date check
us_min = us_data['date'].min()
uk_min = uk_data['date'].min()
jp_min = jp_data['date'].min()
start_date = max(us_min, uk_min, jp_min)
print(start_date)
