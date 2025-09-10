#Loops in Python:

# --- 1) For Loop: ---
# This loop is used when we have the idea of the number of iterations to be done
# The iteration conditions are all written inside the for loop itself

#Basic syntax:
emperor = "Whitebeard"
for i in emperor:       #for every character in the given string, perform the following task:
    print(i, end=", ")

print("Nested For Loop")
commanders = ["Marco", "Ace", "Jozu", "Vista", "Izou"]
for commander in commanders:        #for every element in the given list, perform the following task:
    print(commander)
    for i in commander:
        print(i)

#range() function:
for k in range(5):      #for every integer in the given range, perform the following task:
    print(k)        #0, 1, 2, 3, 4 -> 0 to n-1 by default
print()
for p in range(5):
    print(p+1)      #1, 2, 3, 4, 5
print()
for x in range(1,11):
    print(x)        #1, 2, ..., 10 -> range(starting point, ending point - 1), i.e, range(m, n-1)
print()
for iterate in range(1, 10, 2):
    print(iterate)  #1, 3, 5, 7, 9 -> range(start: int, stop: int, step: int=...)

print("For - Else:")
for a in range (1,5):   #1, 2, 3, 4
    print(a)
else:               #When the condition fails and it will not enter the for loop, it will execute the else part
    print("I am inside else")


# --- 2) While Loop: ---
# Initialization of the element that is to be checked in the while condition
# is necessarily done before the start of the while loop
# and the condition is defined inside the while loop
# inside which a logical block of code is written such that the loop is iterated finite number of times
print("\n")
count = 0 #Variable initialization for condition checking

print("Incremental While Loop:")
while(count <= 5):      #0, 1, 2, 3, 4, 5
    print(count)
    count += 1
print("Decremental While Loop:")
while count > 0:       #5, 4, 3, 2, 1
    print(count)
    count = count - 1

print("While - Else:")
count = 5
while(count >= 0):       #5, 4, 3, 2, 1, 0, I am inside else
    print(count)
    count = count - 1
else:                    #When the condition fails and it will not enter the while loop, it will execute the else part
    print("I am inside else")

# --- Jump Statements in Python: break, continue, pass ---
print("=== FOR LOOP with jump statements ===")
for i in range(1, 7):
    if i == 3:
        print("Encountered 3 → continue (skip this iteration)")
        continue   # skips printing 3. or basically whatever is written below the continue statement and moves to the next iteration condition checking
    if i == 5:
        print("Encountered 5 → break (exit loop)")
        break      # exits/breaks out of the loop completely
    print("Value:", i)
else:
    print("For loop ended normally (no break)")

print("\n=== WHILE LOOP with jump statements ===")
n = 1
while n <= 7:
    if n == 2:
        print("At 2 → pass (do nothing, just a placeholder)")
        pass       # does nothing, just a placeholder
    elif n == 4:
        print("At 4 → continue (skip printing 4)")
        n += 1
        continue   # skips rest of this iteration
    elif n == 5:
        print("At 5 → break (exit loop)")
        break      # exits while loop completely
    print("Value:", n)
    n += 1
else:
    print("While loop ended normally (no break)")


#Note: There is no Do-While Loop in Python
#But sometimes they ask to "Emulate Do-While Loop in Python"
#Here is how to do so:
i = 0
while True:             #Infinite loop
    print(i)
    i += 1              #Will execute at least once

    if(i%100 == 0):     #Condition to break out of the infinite loop
        break



# Thank You!