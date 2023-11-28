class rectangle:
    def __init__(self,l,b):
        self.l1=l
        self.b1=b

    def area(self):
        a=self.l1*self.b1
        return a
    def __lt__(self, obj):
        if (self.area()<obj.area()):
            return "Area of rectangle1 is less than rectangle2"
        elif (self.area()>obj.area()):
            return "Area of rectangle2 is less than rectangle1"
        else:
           return "Area is same"

print("Rectangle 1:")
l1=int(input("Enter the length:"))
b1=int(input("Enter the breadth:"))
obj1=rectangle(l1,b1)
print("Area is",obj1.area())
print("Rectangle 2:")
l2=int(input("Enter the length:"))
b2=int(input("Enter the breadth:"))
obj2=rectangle(l2,b2)
print("Area is",obj2.area())
print(obj1<obj2)