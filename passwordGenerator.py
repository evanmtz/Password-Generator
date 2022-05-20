# Importing random module
import random

# Characters that are going to be used to generate the password.
listOfChar = list("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ`1234567890-=[]\;',./!@#$%^&*()_+}{|:<>?")

# Function to create a password with random characters and specified number of characters.
def getPass():
# Asks user how many characters they'd like their password to have.
    passwordLen = int(input("Enter the amount of characters you'd like your password to have: "))

# for loop that repeats however many times was specified in passwordLen.
    for i in range(passwordLen):
    # Gets a random character from listOfChar and repeats however many times was specified in passwordLen and concatenates the characters to create a password.
        print(random.choice(listOfChar),  end = "")

# Runs getPass() function.
getPass()

# Asks user if they'd like a different password.
diffPass = str(input("\nWould you like to generate a different password? (Yes or no) ")).lower()

# if statement to identify wether user typed yes or no.
# If user input "yes", getPass() function would run again.
if diffPass == "yes":
    getPass()
# else if user input "no", user would recieve "Have a good day!"
elif diffPass == "no":
    print("Have a good day!")