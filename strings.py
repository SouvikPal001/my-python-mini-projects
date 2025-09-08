#Strings in Python
pirate_king = "Luffy"    # Basic example of string variable declaration
right_hand_man = "Zoro"  # A string can be written inside both:-
left_hand_man = 'Sanji'  # A 'single quotation mark' as well as a "double quotation mark"
print(f'\n"{right_hand_man} and {left_hand_man} are the Sword and Shield of {pirate_king}."')
# The reason both type of quotation marks are used is
# to make it easier to print a string that includes quotation marks itself

#Multiline string:
Silvers_Rayleigh = """
"Maybe nothing in this world happens by accident.
As everything happens for a reason,
out destiny slowly takes shape."
"""                                 #Triple single/double quotation marks are used to avoid EOL(End Of Line Error) while compiling
print(Silvers_Rayleigh)

'''
String is "like" an array of characters and are immutable, i.e,
we can print a character by accessing its index but cannot change the content of that index
Note that the indexing of a string starts with zero and end with len(string)-1
'''

#Accessing characters of a string:
print(pirate_king[0]) # L
print(pirate_king[1]) # u
print(pirate_king[2]) # f
print(pirate_king[3]) # f
print(pirate_king[4]) # y
# print(pirate_king[5])    #Error: Index out of bound/String index out of range
# Another, easier way to access each character of a string:
print("Looping through the string:")
for i in pirate_king:
    print(i)
print()

#String Slicing:
wanted = "Nami,Robin"
print(len(wanted)) #length of the string -> 10
print(wanted[0:4]) #including 0 but not 4 -> Nami
print(wanted[1:4]) #including 1 but not 4 -> ami
print(wanted[:4])  #strating from 0 by default upto 4 but not including 4 -> Nami
print(wanted[5:])  #including 5 upto len-1 -> Robin
print(wanted[:])   #traverses the whole string, i.e, from 0 to len-1 -> Nami,Robin
print(wanted[0:-6])  #python reads this as: [0:(len(wanted)-6)] = [0:(10-6)] = [0:4] -> Nami
print(wanted[-1:-5]) #python reads this as: [(len(wanted)-1):(len(wanted)-5)] = [(10-1):(10-5)] = [9:5] which doesn't really make sense so it returns null
print(wanted[-5:-1]) #python reads this as: [(len(wanted)-5):(len(wanted)-1)] = [(10-5):(10-1)] = [5:9] -> Robi
print()

#String methods:
# IMPORTANT NOTE: Keep in mind that strings are immutable,
# so when the following methods are used on the string, it creates an entirely new string and does not mess with the original one
ship = "YOHOHO! The Thousand Sunny!!"
print(len(ship))            #28
print(ship.upper())         #YOHOHO! THE THOUSAND SUNNY!!
print(ship.lower())         #yohoho! the thousand sunny!!
print(ship.rstrip("!"))     #YOHOHO! The Thousand Sunny
print(ship.replace("Thousand Sunny", "Going Merry"))    #YOHOHO! The Going Merry!!
print(ship.capitalize())    #Yohoho! the thousand sunny!!
print(ship.split(" "))      #['YOHOHO!', 'The', 'Thousand', 'Sunny!!']
print(ship.center(50))      #           YOHOHO! The Thousand Sunny!!
print(len(ship.center(50))) #50
print(ship.count("n"))      #3
print(ship.count("o"))      #1, case-sensitive
print(ship.startswith("YOHO"))  #True
print(ship.endswith("!"))   #True
print(ship.startswith("sand", 16, 20))    #True
print(ship.endswith("nny", -5, -2))     #True
print(ship.find("The"))     #8 (starting index of the given word/character
print(ship.find("Zoro"))    #-1 (Zoro not found XD)
print(ship.index("The"))    #8
#print(ship.index("Zoro"))  #Will raise "ValueError: String not found", hence exception handling needed
print(ship.isalnum())       #False, this function returns true only when the given string only consists of characters A-Z, a-z, 0-9
print(ship.isalpha())       #False, this function returns true only when the given string only consists of characters A-Z, a-z
print(ship.islower())       #False, true when all the characters of the given string is in lower case
print(ship.isprintable())   #True, false when the given string contains characters like some escape sequence characters
print(ship.isspace())       #False, true only when all the characters of the given string contains white spaces only
print(ship.title())         #Yohoho! The Thousand Sunny!!
print(ship.istitle())       #True only when each word of the given string is capitalized, i.e, each word's first letter is capital
print(ship.swapcase())      #yohoho! tHE tHOUSAND sUNNY!!

#That is all about strings for now
#Thank you!