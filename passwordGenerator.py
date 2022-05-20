#PASSWORD GENERATOR
# Importing modules
from colorama import Fore, Style
import random, os, sys, time

# Lists
listOfChar = list("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ`1234567890-=[]\;',./!@#$%^&*()_+}{|:<>?")

listOfCol = [Style.BRIGHT, Fore.White, Fore.RED, Fore.BLUE, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX]

# Function used to clear program output when necessary.
def clear():
    os.system("clear")
    
# Function to generate a random password
def getPass():
    
    # Variable to store the password
    password = ""
    
    # Asks user what length they'd like their password to be.
    passwordLen = int(input(Style.RESET_ALL + "Input the amount of characters you'd like your password to have.\n\nIf the length of your password is irrelevant, input 999.\n\n"))

    # Evaluates user input
    if passwordLen == 999:
        
        # 8-21 = Recommended length of a password 
        passwordLen = random.randint(8, 21)
        
    elif passwordLen < 0 or passwordLen == 0:
        clear()
        print("Please input a number greater than 0.")
        time.sleep(3)
        clear()
        getPass()
        
    # Clears any previous console output
    clear()

    # Cool little typing animation (lines 40-51)
    animation1 = "Your generated password is"
    animation2 = "..."
    
    for char in animation1:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(0.05)

    for char in animation2:
        print(char, end = "")
        sys.stdout.flush()
        time.sleep(1)
    
    # Prints new line
    print("\n")
    
    # For loop that generates the password.
    for i in range(passwordLen):
        password = random.choice(listOfChar)
        
    print(password)

    # Runs getPass2 function
    getPass2()

# Function to assure the user of his new generated password.
def getPass2():

    # Asks user if they're satisfied with their password.
    diffPass = input("\nWould you like a different password?\n\n").lower()

    # If statements to evaluate user input.
    if diffPass == 'yes' or diffPass == 'y':
        clear()
        getPass()
        
    elif diffPass == 'no' or diffPass == "n":
        clear()
        farewell1 = "Alright! Wait for it"
        farewell2 = "..."
        for i in farewell1:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
            
        for i in farewell2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(1)

        # Farewell!
        while True:
            print(random.choice(listOfCol) + "Have a good day!", end = " ")

    # Unwanted user input.
    elif diffPass != "yes" and "no":
        clear()
        print("Please input yes/y or no/n next time.")
        time.sleep(3)
        
        restart = input("\nInput 'restart' to restart the program.\n\n").lower()

        if restart == "restart":
            clear()
            getPass()
        else:
            clear()
            print(Fore.RED + "You've terminated the prorgam.\n")
            time.sleep(2)
            print(Style.RESET_ALL + "Click Run to restart the program.\n")
            while True:
                break

# Introduction
intro = (Style.BRIGHT + "Welcome to my Password generator!\n\n")

# Prints intro with typing animation
for char in intro:
# For reference: sys.stdout.write(i) = print(i, end = '')
    print(char, end = '')
    sys.stdout.flush()
    time.sleep(0.05)

# Pauses the console output for said seconds
time.sleep(2)

# Function getting executed to start the password generator
getPass()
