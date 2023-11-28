class time:
    def __init__(self,h,m,s):
        self.h1=h
        self.m1=m
        self.s1=s
    def __add__(self,t2):
        self.hr=self.h1+t2.h1
        self.min=self.m1+t2.m1
        self.sec=self.s1+t2.s1
        if(self.sec>=60):
            self.sec=self.sec-60
            self.min=self.min+1
        if (self.min >= 60):
            self.min = self.min - 60
            self.hr = self.hr + 1

        print(self.hr,":",self.min,":",self.sec)
print("enter first time")
h1=int(input("enter the hour"))
m1=int(input("enter the minute"))
s1=int(input("enter the second"))
t1=time(h1,m1,s1)
print("enter the second time")
h2=int(input("enter the hour"))
m2=int(input("enter the minute"))
s2=int(input("enter the second"))
t2=time(h2,m2,s2)
print("sum of times are:")
t1+t2