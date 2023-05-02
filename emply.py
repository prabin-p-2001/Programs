class Comp:
    def __init__(self,name,id,c_name,d_name):
        self.name=input("\nEnter employee name:")
        self.id=int(input("Enter id: "))
        self.c_name=input("Enter company name: ")
        self.d_name=input("Enter department name: ")

    def display(self):
        print("\nemployee name:",self.name)
        print("\nemployee id:",self.id)
        print("\ncompany name:",self.c_name)
        print("\ndepartment name:",self.d_name)
    
list=[]
while True:

    print("\n1.add employee \t2.display \t3.exit")
    ch=int(input("Enter choice:"))

    if ch==1:
        x=Comp("name",id,'c_name','d_name')
        list.append(x)

    elif ch==2:
        id=int(input("Enter employee id:"))
        for i in list:
            if i.id==id:
                i.display()
                break
        else:
            print("invalid")
            
    elif ch==3:
        print("exited")
        exit()
    else:
        print("invalid choice")
