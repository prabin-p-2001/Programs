import re
s="sat mat pat rat cat"
x=re.findall("[^spr]at",s)
print(x)
