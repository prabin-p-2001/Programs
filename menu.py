l={'jeans':'500','shirt':'400','t-shirt':'300'}
print("\nList")
print("\n1jeans \n2.shirt \n3.t-shirt \n4.exit \n5.cancel all purchase")
a=0
b=0
c=0
while True:

    ch=int(input("\nEnter your choice:"))

    if ch==1:
        print("Choose the item:-jeans")
        a+=int(l['jeans'])
        print("price:",a)

    elif ch==2:
        print("Choose the item:-shirt")
        b+=int(l['shirt'])
        print("price:",b)

    elif ch==3:
        print("Choose the item:-jeans")
        c+=int(l['t-shirt'])
        print("price:",c) 
          
    elif ch==4:
        print("Exited")
        break
    elif ch==5:
        print("Cancelled")
        print(exit())

    else:
        print("\nInvalid choice\ntry again")


      
t=int(int(a)+int(b)+int(c))
print("\n\t\t\ttotal amount:",t)
