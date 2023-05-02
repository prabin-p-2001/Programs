def fib(n):
    a=0
    b=1
    c=0
    print()
    print("fibonacci series")
    print()
    print(a,b,end=' ')
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
    print()
fib(n=int(input("Enter the limit: ")))
