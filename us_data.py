import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data
all_data = pd.read_csv('data/all_data.csv')

#Slice US 
us_data = all_data[all_data.country_region_code == 'US']

plt.scatter(us_data['date'], us_data['grocery_and_pharmacy_percent_change_from_baseline'])
plt.show()
