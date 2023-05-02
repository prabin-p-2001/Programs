str=input("Enter the string: ")
l=len(str)
for i in range(l):
    for j in range(0,i+1):
        print(str[j],end='')
    print()
