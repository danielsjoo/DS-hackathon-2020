import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import CSV data from file
all_data = pd.read_csv('data/all_data.csv')

''' Determine major trends '''
# @axes: x = date, y = normalized change (%?)

# Anchor point +/- tolerance
# If point is cumulative +/- tolerance, mark as trend & set new anchor @ point
# If point is final point, mark as trend and end

TOLERANCE = 50

change_by_date = all_data[['date', 'grocery_and_pharmacy_percent_change_from_baseline']]

#anchor = change_by_date[0]['grocery_and_pharmacy_percent_change_from_baseline']
current = 0
anchor_idx = [0]
length = change_by_date.shape[0]

for i in range(1, length):
    if change_by_date['grocery_and_pharmacy_percent_change_from_baseline'][i] != 'nan':
        current += change_by_date['grocery_and_pharmacy_percent_change_from_baseline'][i]

    print(current)
    if current >= TOLERANCE or current <= -TOLERANCE:
        anchor_idx.append(i)
        current = 0

    i += 1

# Append last point as anchor if needed
if anchor_idx[-1] != length - 1:
    anchor_idx.append(length - 1)

print(anchor_idx)