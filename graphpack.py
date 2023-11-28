from graphics.circle import *
from graphics.rectangle import *
from graphics.dgraphics.cuboid import *
from graphics.dgraphics.sphere import*
r=int(input("Enter the radius of circle:"))
carea(r)
cperi(r)
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rarea(l,b)
rperi(l,b)
l=int(input("Enter the length of cuboid:"))
b=int(input("Enter the breadth of cuboid:"))
h=int(input("Enter the height of cuboid:"))
cuarea(l,b,h)
cuperi(l,b,h)
r=int(input("Enter the radius of sphere:"))
sarea(r)
speri(r)