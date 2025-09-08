#Conditions in Python:
#Conditional Operators: ==,!=,>,<,>=,<=
#Conditional Statements: if, if-else, if-elif-else, nested if-elif-else
#Note: In python, indentation is important because {} aren't used to indicate where the block of code belongs


# Program to demonstrate all conditional statements

# Take an integer input
n = int(input("Enter a number: "))

# --- Simple if ---
if n > 0:
    print("The number is positive.")

# --- if-else ---
if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# --- if-elif-else ---
if n == 0:
    print("The number is zero.")
elif n > 0:
    print("The number is greater than zero.")
else:
    print("The number is less than zero.")

# --- Nested if ---
if n != 0:
    if n > 1:
        print("The number is greater than one.")
    else:
        print("The number is either 0 or 1.")
else:
    print("The number is exactly zero.")

print("Conditional Statements Demonstration Completed.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Greetings Message
import time
timestamp = int(time.strftime('%H'))
if (timestamp >= 4) and (timestamp < 12):
    print("Good Morning!")
elif (timestamp >= 12) and (timestamp < 16):
    print("Good MAfternoon!")
elif (timestamp >= 16) and (timestamp < 21):
    print("Good Evening!")
else:
    print("Good Night!")

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Match Case Statement (Python 3.10 onwards):
choice = int(input("Enter a number between 1 and 5: "))

match choice:
    case 1:
        print("You chose One")  #In python, there is no need to include break statement after each case, if one case is matched, that's it, it won't go any further and come out of the match cases
    case 2:
        print("You chose Two")
    case 3:
        print("You chose Three")
    case 4:
        print("You chose Four")
    case 5:
        print("You chose Five")
    case _:
        print("This is the default case.")
#Thank you!