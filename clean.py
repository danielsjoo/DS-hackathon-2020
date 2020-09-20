import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#retrieve data 
policy_data = pd.read_csv('data/govt_data.csv')
us_data = policy_data[policy_data.country_name == 'United States']
uk_data = policy_data[policy_data.country_name == 'United Kingdom']
cn_data = policy_data[policy_data.country_name == 'China']