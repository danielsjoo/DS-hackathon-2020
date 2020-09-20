import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data
all_data = pd.read_csv('data/all_data.csv')

#Slice US 
us_data = all_data[all_data.country_region_code == 'US']


