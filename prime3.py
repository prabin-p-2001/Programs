l=int(input("Enter the limit: "))
for i in range(1,l+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
