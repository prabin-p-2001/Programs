n=int(input("Enter two or more digits: "))
s=0
d=0
while n>0:
    d=n%10
    s+=d
    n=n//10
print("sum is:",s)
