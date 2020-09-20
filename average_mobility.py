import csv

us_gov = open("data/uk_mobility.csv")
output = open("data/uk_mobility_average.csv", 'w')

r = csv.reader(us_gov)
w = csv.writer(output)

i,j,k,l,m=0,0,0,0,0
a,b,c,d,e = 0,0,0,0,0
date = "2/15/2020"

for row in r:
    if row[0] == "3/28/2020":
        continue
    if row[0] == date:
        if row[2] != "":
            a += float(row[2])
            i = i+1
        if row[3] != "":
            b += float(row[3])
            j += 1
        if row[4] != "":
            c += float(row[4])
            k += 1
        if row[5] != "":
            d += float(row[5])
            l += 1
        if row[6] != "":
            e += float(row[6])
            m += 1
    else:
        w.writerow([date, row[1] , round(a/i,2), round(b/j,2), round(c/k,2), round(d/l,2), round(e/m,2)])
        date = row[0]
        print (row[6])
        if row[2] != "":
            a = float(row[2])
        else:
            a = 0
            #this is obviously wrong and bad, but it only affects at most 1/412 points in very few days of the year
        if row[3] != "":
            b = float(row[3])
        else:
            b = 0
        if row[4] != "":
            c = float(row[4])
        else:
            c = 0
        if row[5] != "":
            d = float(row[5])
        else:
            d = 0
        if row[6] != "":
            e = float(row[6])
        else:
            e = 0
        i=1
    

us_gov.close()
output.close()