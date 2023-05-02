s=input("Enter the string: ")
dict={}
for i in s:
    keys=dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)
