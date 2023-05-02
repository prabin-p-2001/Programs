n1=int(input("\nEnter the first number:"))
n2=int(input("Enter the second number:"))
for i in range(1,5):
    print("\n1.Addition 2.subtraction 3.multiplication 4.division 5.exit")
    c=int(input("\nSelect your choice:"))

    if c==1:
        sum=n1+n2
        print("\nsum is:",sum)
    elif c==2:
        sub=n1-n2
        print("\nsubtraction is",sub)
    elif c==3:
        mul=n1*n2
        print("\nmultiplication is",mul)
    elif c==4:
        div=n1/n2
        print("\ndivision is",div)
    elif c==5:
        print(exit())
    else:
        print("\ninvalid choice!")
