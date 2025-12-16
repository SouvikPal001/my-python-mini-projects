#1) Write a python function to reverse a string without slicing or reverse() function:
def reverse_string(data):
    result = ""
    for char in data:
        result = char + result
    return result

print(reverse_string(data = 'Luffy'))
#=======================================================================================================================
#2) WAP to delete all consonants from a given string:
def return_string(data):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in data if not char.isalpha() or char in vowels])
    return result

print(return_string(data = "One Piece Is Real!"))
#=======================================================================================================================
#3) Sum of all numbers between 1 and N:
def is_prime(number):
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

def add(number):
    total = 0
    for i in range (2, (number + 1)):
        if is_prime(i):
            total = total + i
    return total

print(add(number = 30))
#=======================================================================================================================
#4) Swap two variables:
#Method 1(Traditional):
a = 20
b = 10
temp = a
a = b
b = temp
print(a,b)

#Method 2(Using 2 variables only):
a = 20
b = 10
a = a*b     #OR a+b
b = a/b     #OR a-b
a = a/b     #OR a-b
print(a,b)

#Method 3(Python special):
a, b = 20, 10
a, b = b, a
print(a, b)
#=======================================================================================================================
#5) Factorial of a number(Recursion):
def factorial(number):
    if number == 0:
        return 1
    elif number > 0:
        return number * factorial(number - 1)
    else:
        print("Factorial of negative numbers aren't possible")
        return None

print(factorial(number = 5))
#=======================================================================================================================
#6) Fibonacci series:
def fibonacci(number):
    series = [0, 1]
    while len(series) < number:
        series.append(series[-1] + series[-2])
    return  series

print(fibonacci(10))
#=======================================================================================================================
#7) Extraction of digits of given number:
num = int(input("Enter a number: "))
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num//10
#=======================================================================================================================
#8) 