l=0
while l<3:
    n=int(input("Enter the number:"))
    if n==1:
        print("not prime")
    elif n>1:
        for i in range(2,n):
            if n%2==0:
                print("not prime\n")
                break
        else:
            print("prime\n")
    l+=1
