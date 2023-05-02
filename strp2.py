s=input("Enter the string: ")
c=input("Enter character to check:")
ct=0
for i in s:
    if i==c:
        ct=ct+1
print(c,"in",ct,"times")
