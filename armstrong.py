n=int(input("Enter the number:"))
t=n
s=0
while n>0:
    digit=n%10
    r=digit**3
    n=n//10
    s+=r
   
if s==t:
    print("armstrong")
else:
    print("not armstrong")

