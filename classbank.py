class bank:
    def __init__(self,acc,name,type):
        self.ac=acc
        self.name=name
        self.type=type
        self.bal=0
    def Deposit(self,bld):
        self.bal=self.bal+bld
    def Withdraw(self,blw):
        if(self.bal<blw):
            print("insufficient balance")
        else:
            self.bal=self.bal-blw
        print("Current balance is",self.bal)
    def Display(self):
        print("Account number:",self.ac)
        print("Account Holder:",self.name)
        print("Account Type:",self.type)
        print("Account Balance:",self.bal)

acc=int(input("enter the account no.:"))
name=input("enter the name of the account holder:")
type=input("enter the type of the account:")
bld=int(input("enter the amount to deposit:"))
P=bank(acc,name,type)
P.Deposit(bld)
P.Display()
blw=int(input("enter the amount to withdraw"))
P.Withdraw(blw)




