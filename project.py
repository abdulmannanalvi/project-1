computer = -1
youstr = input("Enter your choice: ") 
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]
if (computer == you):
    print("Draw")
else:
    if(computer ==-1 and you ==1): 
        print("You Win!")
    elif(computer ==-1 and you ==0): 
        print("You Lose!")

    if(computer ==1 and you ==-1): 
        print("You Lose!")
    elif(computer ==1 and you ==0):
        print("You Win!")

    if(computer ==0 and you ==-1): 
        print("You Lose!")
    elif(computer ==0 and you ==1):
        print("You Win!")

    else:
        print("Something went Wrong")