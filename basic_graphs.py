import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime as dt

# Import CSV data from file
us_stringency = pd.read_csv('data/us_gov_averaged.csv')
us_stringency.date = pd.to_datetime(us_stringency.date)
us_mobility = pd.read_csv('data/us_mobility_average.csv')
us_mobility.date = pd.to_datetime(us_mobility.date)

jp_stringency = pd.read_csv('data/jp_gov_averaged.csv')
jp_stringency.date = pd.to_datetime(jp_stringency.date)
jp_mobility = pd.read_csv('data/jp_mobility_average.csv')
jp_mobility.date = pd.to_datetime(jp_mobility.date)

uk_stringency = pd.read_csv('data/uk_gov_averaged.csv')
uk_stringency.date = pd.to_datetime(uk_stringency.date)
uk_mobility = pd.read_csv('data/uk_mobility_average.csv')
uk_mobility.date = pd.to_datetime(uk_mobility.date)

# TODO: deaths/time, cases/time, mobility/time graphs

def make_time_graph(dataset, metric, ylabel, title):
    model = LinearRegression()
    x = dataset['date'].map(dt.datetime.toordinal).to_numpy().reshape(-1, 1)
    model.fit(x, dataset[metric])
    y = model.predict(x)

    plt.figure(figsize=(8, 6))
    plt.scatter(dataset['date'], dataset[metric], s=8)
    plt.plot(x, y, color='red')
    plt.xlabel('Date (YYYY-MM)')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

mobility_flavors = ['grocery_and_pharmacy', 'parks', 'transit_stations', 'workplaces', 'residential']
mobility_labels = ['Mobility Changes (G&P)', 'Mobility Changes (Parks)', 
                    'Mobility Changes (Transit)', 'Mobility Changes (Workplaces)',
                    'Mobility Changes (Residential)']

#make_time_graph(us_stringency, 'deaths', 'Deaths', 'US Deaths vs. Time')
#make_time_graph(us_stringency, 'confirmed_cases', 'Confirmed Cases', 'US Confirmed Cases vs. Time')
for i in range(len(mobility_flavors)):
    make_time_graph(us_mobility, mobility_flavors[i], 'Average Change in Mobility (%)', 'US ' + mobility_labels[i])

#make_time_graph(uk_stringency, 'deaths', 'Deaths', 'UK Deaths vs. Time')
#make_time_graph(uk_stringency, 'confirmed_cases', 'Confirmed Cases', 'UK Confirmed Cases vs. Time')
for i in range(len(mobility_flavors)):
    make_time_graph(uk_mobility, mobility_flavors[i], 'Average Change in Mobility (%)', 'UK ' + mobility_labels[i])

#make_time_graph(jp_stringency, 'deaths', 'Deaths', 'JP Deaths vs. Time')
#make_time_graph(jp_stringency, 'confirmed_cases', 'Confirmed Cases', 'JP Confirmed Cases vs. Time')
for i in range(len(mobility_flavors)):
    make_time_graph(jp_mobility, mobility_flavors[i], 'Average Change in Mobility (%)', 'JP ' + mobility_labels[i])

def make_mobility_graph():
    pass

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