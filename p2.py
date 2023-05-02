n=int(input("Enter the limlit: "))
for j in range(n+1):
    print("*"*j,end='')
    print()

for i in range(n+1,0,-1):
    print("*"*i,end='')
    print() 

for k in range(1,n+1):
    print(" "*(n-k)+"*"*k)


for a in range(n+1,0,-1):
    print(" "*(n-a)+"*"*a)


for x in range(0,n):
    print(" "*(n-x)+"*"*((2*x)+1))
    
for y in range(n,-1,-1):
    print(" "*(n-y)+"*"*((2*y)+1))
    
