iteration=True
while iteration==True:

    import random


    def swg_game(cam, you):
        if cam == you:
            return 'No'
        elif cam == 's':
            if you == 'w':
                return False
            elif you == 'g':
                return True
        elif cam == 'w':
            if you == 's':
                return True
            elif you == 'g':
                return False
        elif cam == 'g':
            if you == 's':
                return False
            elif you == 'w':
                return True


    print("\n...WELL TO SNAKE, WATER AND GUN GAME ....\n")
    v=input("Please, press 'Enter' to start the game...\n")
    camp = print("\ncomputer's turn: snak(s) , water(w) or gun(g) ?")
    rd = random.randint(1, 3)
    if rd == 1:
        camp = 's'
    elif rd == 2:
        camp = 'w'
    elif rd == 3:
        camp = 'g'

    print("Computer turn is over Now :")
    your = input(
        "\nyour turn: snak(s) , water(w) or gun(g)?\nChoose your option from the given above :\n")

    a = swg_game(camp, your)
    print("computer choose :- ", camp)
    print("you choose :- ", your)

    if a == 'No':
        print("\nGame is tie..\n")
    elif a == True:
        print(" \nYou win the game...  \n")
    elif a == False:
        print("\nYou lose the game...\n")
    else:
        print("\nSomething went rong pleaas try again...\n")

    
    v=input("'Enter' to play again , 'q' to quit the game\n ").lower()

    if v=='q':
        break
    else:
        continue

