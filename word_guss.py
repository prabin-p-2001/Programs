import random
word_list=['apple','orange','banana']
c=random.choice(word_list)
t=5
guss_list=[]

while t>0:
    display=""
    for l in c:
        if l in guss_list:
            display+=l
        else:
            display+='_ '

    print(display)


    guss=input("\nGuss a letter: ").lower()
    if guss in guss_list:
        print("\nyou already gussed that letter!")
        continue
    guss_list.append(guss)

    if guss in c:
        print("\ncorrect guss")
    else:
        print("\nwrong guss")
        t-=1

    if '_' not in display:
        print("\nyou win")
        break
        
    elif t==0:
        print("\nyou lose")
        break
        
    print("\ntries left",t)
    


            

