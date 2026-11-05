
import random

score = 0

# Create a simple game round
def play_game(round_number):

    global score

    aliens = 3 + round_number

    print("\nROUND", round_number)
    print("Aliens remaining:", aliens)

    while aliens > 0:

        print("\nScore:", score)
        print("Aliens:", aliens)

        choice = input("Press S to shoot or Q to quit: ").lower()

        if choice == "q":
            return False

        elif choice == "s":

            if random.randint(1, 2) == 1:
                aliens -= 1
                score += 10
                print("You hit an alien! +10 points")

            else:
                print("You missed!")

        else:
            print("Invalid choice!")

    print("You defeated all the aliens!")
    return True


# LEVEL 1: INFINITE WHILE LOOP
def level_one():

    round_number = 1

    print("\nLEVEL 1: INFINITE MODE")

    while True:

        result = play_game(round_number)

        if result == False:
            break

        round_number += 1

    print("Level 1 finished!")
    print("Final score:", score)


# LEVEL 2: FINITE FOR LOOP
def level_two():

    print("\nLEVEL 2: FIVE ROUNDS")

    for round_number in range(1, 6):

        result = play_game(round_number)

        if result == False:
            break

    print("Level 2 finished!")
    print("Final score:", score)


# MAIN MENU
print("\nSPACE INVADERS")
print("1. Infinite Game")
print("2. Five Round Game")

choice = input("Choose a level: ")

if choice == "1":
    level_one()

elif choice == "2":
    level_two()

else:
    print("Goodbye!")






for round_number in range(1, 6):
    result = play_game(round_number)




    while True:
    result = play_game(round_number)