class bank:
    def __init__(self,ac,name,bal):
        self.ac=int(input("Enter the a/c no:"))
        self.name=input("Enter your name:")
        self.bal=int(input("Enter balance:"))

    def deposit(self):
        n=int(input("Enter amount:"))
        self.bal=self.bal+n
        

    def withdraw(self):
        n=int(input("Enter amount:"))
        self.bal=self.bal-n
        
    def balance(self):
        print("balance is:",self.bal)
        


l=[]
print("\n1.Create a/c \t2.deposit \t3.withdraw \t4.balance \t5.exit")
while True:
    
    ch=int(input("\nEnter your choice:"))

    if ch==1:
        x=bank(1,"name",100)
        l.append(x)


    elif ch==2:
        an=int(input("Enter a/c no:"))
        for x in l:
            if x.ac==an:
                x.deposit()
                break
        else:
            print("invalid a/c no") 
                

    elif ch==3:
        an=int(input("Enter a/c no:"))
        for x in l:
            if x.ac==an:
                x.withdraw()
                break
        else:
            print("invalid a/c no")
            

    elif ch==4:
        an=int(input("Enter a/c no:"))
        for x in l:
            if x.ac==an:
                x.balance()
                break
        else:
            print("invalid a/c no")
            

    elif ch==5:
        exit()

    else:
        print("Invalid choice")
