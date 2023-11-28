import csv
c=open("csv3.csv", newline='')
d = csv.DictReader(c)
print("ROLL NO  and STUDENT NAME")
for i in d:
    print(i['ROLL NO'], i['STUDENT NAME'])
    