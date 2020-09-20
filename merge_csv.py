import csv

w1 = open("data/us_mobility.csv")
csvfile = open ("data/Covid_govt_data.csv")
output = open("data.us_all_data.csv", 'w')

r = csv.reader(csvfile)
r2 = csv.reader(w1)
w = csv.reader(output)

i = 0
for row in r:
    for row2 in r2:
        if row2[0] == "United States":
            
        writer1.writerow([row[0],row[2],row[3], row[4], row[5], row[6], row[7]])
    

w1.close()
w2.close()
w3.close()
csvfile.close()