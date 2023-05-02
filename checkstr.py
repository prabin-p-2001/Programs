def check(w):
    c=0
    v=['a','e','i','o','u']
    for i in w:
        if i in v:
            c+=1
    print("The no of vowels ",c)

check(w=input("Enter the string: "))
