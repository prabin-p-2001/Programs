print("lorem ipsum is a simple dummy text\n")

a="lorem ipsum is a simple dummy text"
b=a.split()
d=''
for c in b:
    d+=''.join(sorted(c)) + ' '
print(d)
