import re
s="1 12 123 1234 12345"
x=re.findall("\d\d\d\d+",s)
print(x)
