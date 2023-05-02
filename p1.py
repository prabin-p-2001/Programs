#   PATTERN 1

n=int(input("Enter max-rows:"))
num=1
for i in range(0,n+1):
    for j in range(1,i+1):
        print(num,end=' ')
        num+=1
    print()
# 
# 
#    PATTERN 2

n=int(input("Enter max-rows:"))
for i in range(0,n+1):
    for j in range(1,n+1):
        print('*',end='')
    print()



#   PATTERN 3
n=int(input("Enter max-rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(j,end='')
    print()


n=int(input("Enter max-rows:"))
a=1
for i in range(0,5):
    for j in range(0,i+1):
        print(a,end='')
    a+=1
    print()
