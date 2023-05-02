def fact(n):
    f=1
    if n==1:
        f=1
        return f
    else:
        f=n*fact(n-1)
    return f

n=int(input("Enter:"))
res=fact(n)
print(res)
