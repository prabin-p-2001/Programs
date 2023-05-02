s= "abaabbabab"
t= ""
n=len(s)

for i in range(0,len(s)):
    if s[i]=="a":
        t+="a"
        
            
    if s[i]=="b":
        t+="b"
        break
        
    print(t)
    
