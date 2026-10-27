def vendingmachine():
    print("VENDING MACHINE IS ON...")
    print("Please enter a vending value to get an item: ")
    item = input()
    while item != "q":
        if item == "b3":
            print("nacho chips")