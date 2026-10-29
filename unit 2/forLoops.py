# what is a loop --> code that repeats.

# while loops = a block code thats repeats itself until the triggering
# condition is no longer TRUE. CAN BE INFINITE.

# for loops = a type of loop, but
# it only repeats itself upto a certain number of times.
# IT IS FINITE

# think of for loops as the counting loop = for --> 4 = number of loop

# for loop syntax
# i stand for iterator = programmers decided to make this the universal
# placeholder for counting

run: "to walk really fast."
def counting():
    # this is what i want you to do...

for i in range(1,5):
        print(i)

for i in "school":
        print(i)

# list --> a collection type that acts as container for
# multiple data types and pieces of data.

# list syntax
# a list is written like a variable BUT after the equal assignment
# symbol we use SQUARE BRACKETS and put all of the datas inside of 
# them

fooditem= "popcorn"

grocerylist = ["popcorn", "apples", "water", "chips", "fish", "celery"]

for i in grocerylist:
        print("i need to buy " + str(i))

itemprices = [10.00, 20.00, 13.25, 7.95, 349.00]
tax = 0.07
semestergrades = [90, 100, 78, 76, 74, 82, 84]

for i in semestergrades:
        # i want to find ALL the grades lower 85.
        if grade < 85:
                print(grade)
fruits = ["apples", "bananas", "cherry"]

for i in fruits:
        print(i)
        break
