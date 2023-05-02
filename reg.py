import re
txt=input("Enter:")
x=re.findall("[a-z]+[0-9]+[_&]?[@]?[a-z]+[.]{1}+[a-z]{2,3}",txt)
if x:
    print("valid")
else:
    print("invalid")
