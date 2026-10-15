# conditional if/else logic- these are two words that intrust your
# program to do specifice intrust based on specific data
# or conditions


def calculate_add():
    print("Program has started: type in 2 numbers to add: ")
    num1= int(input())
    num2= int(input())
    print(num1 + num2)
    print("Program has ended.")

def calculate_multiply():
    print("Program has started: type in 2 numbers to multiply: ")
    num1= int(input())
    num2= int(input())
    print(num1 * num2)
    print("Program has ended.")

def calculate_subtract():
    print("Program has started: type in 2 numbers to subtract: ")
    num1= int(input())
    num2= int(input())
    print(num1 - num2)
    print("Program has ended.")

def calculate_divide():
    print("Program has started: type in 2 numbers to divide: ")
    num1= int(input())
    num2= int(input())
    print(num1 / num2)
    print("Program has ended.")

    def mainCalculator():
        # take in a user selection as a number
        selection= input()

        if selection ==1:
            calculate_add()
        elif selection == 2:
            calculate_subtract()
         elif selection ==3:
             calculate_divide()
        elif selection == 4:
            calculate_multiply()
        else: 
            print("Sorry something went wrong.")


    def movie_ticket_ammount():
        print("Welcome to the movie threater. How old are you?")
        age = input()

        if age < 7:
            print("Your ticket is $8.00")
        elif age > 8 and age < 20
            print("your ticket is $12.00")
        elif age > 21 and age < 60:
            print("your ticket is $20.00")
        elif age > 61:
            print("your ticket is $20.00")
        else:
            print("Sorry invalid input")

        movieTicketprice()