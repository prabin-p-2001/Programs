s=input("Enter")
l=len(s)
k=''
r=''
for i in range(l):
    k=s[0:2]+s[-2:]
    if i!=l:
        r='.'.join(k)
print(r)
