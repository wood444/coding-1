# loop - a loop is a construct(special function) that repeats itself.
# In programming, a loop allows to repeat code instructions.

# There are two types of loops: For loops and While loops

# While loop - a type of loop where so long as a condition is equal
# to true it will keep running "forever".

# the key is while --> do while

# syntax
num = 4
while 2+2 == num: #condition --> operations - must be true
    print("the program is running...")
    num = int(input("please type in a number: "))

# while loops will ALWAYS run unless you change the condition!
# we can do this by writing instructions to manually change it.

def guessingGame():
    correctAnswer = 12
    attempts = 0

    print("GUESSING GAME HAS STARTED")
    userGuess = input("Please guess a number between 1 and 50.")

    while userGuess != correctAnswer:
        print("incorrect. Please try again...")
        print("GUESS attempts: " + str(attempts))
        userGuess = int(input("Please guess a number between 1 and 50."))
    
    guessingGame()










# Question 1
def guessingPassword():
    correctPw = 112110
    print("Please log in with your password...")
    attempts = 4
    userPwAttempt = input()

    while userPwAttempt != correctPw:
        print("password incorrect.")
        print("try again")
        print("Please log in with your password...")
        attempts -= 1
        print("you have this many attempts left: "+str(attempts))
        userPwAttempt = input()
    print("welcome you have access...")

guessingPassword()