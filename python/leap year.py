fyear=int(input("enter the initial year"))
lyear=int(input("enter the  final year"))
print("leap years are:")
for i in range(fyear,lyear+1):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)