import csv

us_gov = open("data/uk_gov.csv")
output = open("data/uk_gov_averaged.csv", 'w')

r = csv.reader(us_gov)
w = csv.writer(output)

i=0
confirmed_cases = 0
deaths = 0
stringency_index = 0
date = "1/1/2020"

for row in r:
    if row[0] == date:
        i = i+1
        confirmed_cases += float(row[1])
        deaths += float(row[2])
        stringency_index += float(row[3])
    else:
        print(confirmed_cases)
        w.writerow([date, confirmed_cases/i,2, deaths/i,2, stringency_index/i,2])
        date = row[0]
        confirmed_cases, deaths, stringency_index = 0,0,0
    

us_gov.close()
output.close()

