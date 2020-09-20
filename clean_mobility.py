import csv

w1 = open("data/us_mobility.csv", 'w')
w2 = open("data/uk_mobility.csv", 'w')
w3 = open("data/jp_mobility.csv", 'w')
csvfile = open ("data/all_data.csv")

r = csv.reader(csvfile)
writer1 = csv.writer(w1)
writer2 = csv.writer(w2)
writer3 = csv.writer(w3)

for row in r:
    if row[2] == "US":
        writer1.writerow([row[0],row[2],row[3], row[4], row[5], row[6], row[7]])
    elif row[2] == "BG":
        writer2.writerow([row[0],row[2],row[3], row[4], row[5], row[6], row[7]])
    elif row[2] == "JP":
        writer3.writerow([row[0],row[2],row[3], row[4], row[5], row[6], row[7]])

w1.close()
w2.close()
w3.close()
csvfile.close()