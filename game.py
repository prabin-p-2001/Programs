import random
list=['rock','scissors','paper']
computer=random.choice(list)
print("\n\t\tROCK PAPER SCISSORS")
while True:
    ch=input("\n\nEnter your choice\n(rock/paper/scissors/exit): ")
    if ch==computer:
        print("\nGame is tie")
        
    elif ch=='rock' and computer=='scissors':
        print("\nYou win")

    elif ch=='scissors' and computer=='paper':
        print("\nYou win")

    elif ch=='paper' and computer=='rock':
        print("\nYou win")
        
    elif ch=='exit':
        print("\nexited")
        exit()

    else:
        print("\nComputer win")
        
                                                                    
