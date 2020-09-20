import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import CSV data from file
all_data = pd.read_csv('data/all_data.csv')
print(all_data.head())

# Visualize(?)
plt.scatter(all_data['date'], all_data['grocery_and_pharmacy_percent_change_from_baseline'])
plt.show()
