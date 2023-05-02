#pattern-1

n=65
for i in range(0,6):
    for j in range(0,i+1):
        print(chr(n),end='')
    n+=1
    print()





#pattern-2

n=65
for i in range(0,6):
    for j in range(1,i+1):
        print(chr(n),end='')
        n+=1
    print()






#pattern-3

for i in range(0,6):
    for j in range(1,i+1):
        print(chr(j+64),end='')
    print()






#pattern-4

for i in range(0,6):
    for j in range(i,0,-1):
        print(chr(j+64),end='')
    print()
