
import csv
c= open("csv3.csv",newline='')
d=csv.reader(c)
for row in d:
        print(' ,'.join(row))