import csv
field=['No','Company','Model']
cars=[{'No':1,'Company':'Ferrari','Model':'GH'},
      {'No':2, 'Company': 'BMW', 'Model': 'X5'},
      {'No':3, 'Company': 'Audi', 'Model': 'Swift'},
      {'No':4, 'Company': 'Toyota', 'Model': 'Fortuner'}]
r=open('b.csv','w')
write=csv.DictWriter(r,fieldnames=field)
write.writeheader()
write.writerows(cars)
r.close()

c=open('b.csv',newline='')
d=csv.reader(c)
for i in d:
    print(' '.join(i))

