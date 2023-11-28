x=open("demo.txt","r")
y=open("t","w")
r=x.readlines()
ln=len(r)
for i in range(0,ln):
    if(i%2==0):
        y.write(r[i])
y.close()
x.close()
y=open("t","r")
display=y.read()
print(display) 

