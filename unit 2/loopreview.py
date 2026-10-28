def vendingmachine():
    print("VENDING MACHINE IS ON...")
    print("Please enter a vending value to get an item: ")
    item = input()
    while item != "q":
        if item == "b3":
            print("nacho chips")


def diceGame():
    print("DICE GAME")
    print("Type r to roll the dice or q to quit the game: ")
    userselection = input()

    while userselection != 'q':
        if userselection == "r":
           DiceValue = random.randint(1,7)
           if DiceValue == 7
                print("You rolled a: " + str(DiceValue))
                print("YOU LOSE")