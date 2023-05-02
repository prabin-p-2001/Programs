n=int(input("Enter the limit:")) 
for i in range(n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("2",end='')
        else:
            print("1",end='')
        
    print()
    
