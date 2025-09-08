#Introduction To Python
print("Hello, World!")
print('First Python Program')
print(20, "and", 10, sep="_", end=None) #sep is used to separate multiple values and end is used to end the print statement with given string in print(), are not necessary to write everytime

'''
This is a multiple line comment.
"#" is used for single line comment.
Escape Sequence Characters: \n(new line), \t(tab), \r(return), \b(backspace) \', \", \%, \\, etc
'''

"""
This is also a multiple line comment.
Use (ctrl + /) to comment or uncomment any line(s) of code by selecting that desired portion
Both these types of comments are also strings that can be stored in a variable
"""

#Datatypes and Variables
age: int = 20
name: str = "Luffy"
is_student: bool = True
my_variable = None
#It is not necessary but recommended to initialize along with its datatype
a = 10
b = "Boa Hancock"
Pirate_King = True
c = complex(1, 9)
print("Type of a is: ", type(a))
print("Type of b is: ", type(b))
print("Type of Pirate_King is: ", type(Pirate_King))
print(c, " ", type(c))
'''
Built in datatypes in python:
1) Numeric data: int, float, complex'
2) Text data: str
3) Boolean data: bool
4) Sequence data: list, tuple
5) Hashmap(Mapped data): dict
6) Hashset: set
All these are an object in python, hence when we print the type it shows <class>
'''

#Typecasting and User Input 
x = "1"
y = "2"
print(x + y) #12
print(int(x)+int(y)) #3
'''
For typecasting, python supports a wide variety of functions or methods like:
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc
Implicit: Python itself does typecastings, this is why it is not necessary to write types while declaring variables
Explicit: Developer commands python to typecast using above mentioned functions
'''
#z = input() #most basic input code, the cursor will be blinking until you type some input, hence it is recommended to put a message inside the input function
# name = input("Enter your name: ") #By default the input functions takes string as input type
# p = input("Enter first number: ") #20
# q = input("Enter second number: ") #10
# print(p + q) #2010 - concatination of strings
# i = int(input("Enter a number: ")) #25
# j = float(input("Enter another number: ")) #9
# print(type(i - j)) #<class 'float'>


#Operators In Python
"""
1) Arithematic: +, -, *, /, %, **(exponential/raised to power), //(floor division)
2) Assignment: =, +=, -=, *=, /=, %=, **=, //=
3) Comparison/Relational: ==, !=, >, <, >=, <=
4) Logical: and, or, not
5) Bitwise: &, |, ^, ~, <<, >>
6) Identity: is, is not
7) Membership: in, not in
"""
#Calculator Program In Python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
#Of course, this is the most basic calculator program, a real calculator takes an operator as an input too and only provides the required answer
#We will be making a better version of this in the upcoming programs after learning some more python concepts
#Thank you!