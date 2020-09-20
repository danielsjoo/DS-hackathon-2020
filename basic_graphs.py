import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime as dt

# Import CSV data from file
us_stringency = pd.read_csv('data/us_gov_averaged.csv')
us_stringency.date = pd.to_datetime(us_stringency.date)
us_mobility = pd.read_csv('data/us_mobility.csv')

jp_stringency = pd.read_csv('data/jp_gov_averaged.csv')
jp_mobility = pd.read_csv('data/jp_mobility.csv')

uk_stringency = pd.read_csv('data/uk_gov_averaged.csv')
uk_mobility = pd.read_csv('data/uk_mobility.csv')

# TODO: Stringency/mobility, stringency/time, mobility/time graphs

plt.figure(figsize=(8, 6))
plt.scatter(us_stringency['date'], us_stringency['deaths'])

model = LinearRegression()
x = us_stringency['date'].map(dt.datetime.toordinal).to_numpy().reshape(-1, 1)
model.fit(x, us_stringency['deaths'])
y = model.predict(x)

plt.plot(x, y)
plt.show()


'''
# Import CSV data from file
all_data = pd.read_csv('data/all_data.csv')

change_by_date = all_data[['date', 'grocery_and_pharmacy_percent_change_from_baseline']]

# Convert string dates to int dates
dates = pd.to_datetime(change_by_date['date'])
print(dates)
'''
''' Determine major trends '''
# @axes: x = date, y = normalized change (%?)

# Anchor point +/- tolerance
# If point is cumulative +/- tolerance, mark as trend & set new anchor @ point
# If point is final point, mark as trend and end

#TOLERANCE = 100
'''
change_by_date = all_data[['date', 'grocery_and_pharmacy_percent_change_from_baseline']]

model = LinearRegression()
x = np.array([i for i in range(210)]).reshape(-1,1)
model.fit(x, change_by_date['grocery_and_pharmacy_percent_change_from_baseline'])
y = model.predict(x)

plt.scatter(change_by_date['date'], change_by_date['grocery_and_pharmacy_percent_change_from_baseline'])
plt.plot(x, y)
plt.show()
'''
'''
#anchor = change_by_date[0]['grocery_and_pharmacy_percent_change_from_baseline']
current = 0
anchor_idx = [0]
length = change_by_date.shape[0]

plt.scatter(change_by_date['date'], change_by_date['grocery_and_pharmacy_percent_change_from_baseline'])
plt.show()

for i in range(1, length):
    if change_by_date['grocery_and_pharmacy_percent_change_from_baseline'][i] != 'nan':
        current += change_by_date['grocery_and_pharmacy_percent_change_from_baseline'][i]

    #print(change_by_date['grocery_and_pharmacy_percent_change_from_baseline'][i])
    if current >= TOLERANCE or current <= -TOLERANCE:
        anchor_idx.append(i)
        current = 0

    i += 1

# Append last point as anchor if needed
if anchor_idx[-1] != length - 1:
    anchor_idx.append(length - 1)

print(anchor_idx)
'''