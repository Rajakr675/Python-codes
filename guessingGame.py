import random

chances = 0
while chances < 3:
    randm = random.randint(0, 9)    # number will be genreted between (0,9)
    print(randm)
    usrNum = int(input("Guess a number: "))
    if usrNum == randm:
        print("Congrats you won the game :)")
        usrChoice = input("Do wanna play again = yes or no: ")  ## wanna = want to
        if usrChoice == "yes":
            # chances = 0
            continue
        else:
            break
    elif chances == 2:
        print("Sorry, You loose the game :(")
        usrChoice = input("Do wanna play again = yes or no: ")
        if usrChoice == "yes":
            chances = 0     #chanses will be reset
            continue
        else:
            break
    chances+=1
    print("Moves left", 3-chances)