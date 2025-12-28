#Lists in Python
"""
A list is an ordered, mutable collection of items.
Unlike strings, lists CAN be modified after creation.
We use list when we need to store multiple values (possibly of different datatypes) at the same place.
List items are separated by commas and enclosed within [SQUARE BRACKETS].
The index of a list in Python starts from 0 and ends on n-1.
"""

strawhats = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jimbei"]    #Basic declaration and initiation of a list
# Index:       [0]      [1]     [2]     [3]      [4]       [5]       [6]      [7]       [8]       [9]
print(type(strawhats))
strawhats[0] = "Monkey D. Luffy"    #Mutability

anime_details = ["One Piece", 1155, True, 9.5]      #A list can have multiple elements of different datatypes

nakama = []     #Empty list declaration

#Nested List:
bounties = [
    ["Luffy", 3000000000],
    ["Zoro", 1111000000],
    ["Sanji", 1032000000]
]
print("\nNested list:")
for pirate in bounties:
    print(f"{pirate[0]} has a bounty of {pirate[1]} Berries!")


#Accessing elements using indexing:
print("\nAccessing elements:")
print(strawhats[0])    #First element -> Luffy
print(strawhats[1])    #Element present on the given index -> Zoro
print(strawhats[-1])   #Last element -> Jimbei
#How python interprets negative indexes(for easier understanding):
print(strawhats[-4])    #Python reads this as strawhats[len(strawhats) - 4] = strawhats[10 - 4] = strawhats[6] -> Robin
# print(strawhats[10])   #Error: Index out of bound/List index out of range
print()

#List Slicing:
# NOTE: slicing always moves left → right
print(len(strawhats)) #length of the list -> 10
print(strawhats[0:5]) #including 0 but not 5 -> Luffy, ..., Sanji
print(strawhats[1:5]) #including 1 but not 5 -> Zoro, ..., Sanji
print(strawhats[:5])  #stating from 0 by default upto 5 but not including 5 -> Luffy, ..., Sanji
print(strawhats[5:])  #including 5 upto len-1 -> Chopper, ..., Jimbei
print(strawhats[:])   #traverses the whole list (creates a shallow copy), i.e, from 0 to len-1 -> Luffy, ..., Jimbei
print(strawhats[0:-6])  #python reads this as: [0:(len(strawhats)-6)] = [0:(10-6)] = [0:4] -> Luffy, ..., Usopp
print(strawhats[-1:-5]) #python reads this as: [(len(strawhats)-1):(len(strawhats)-5)] = [(10-1):(10-5)] = [9:5] which doesn't really make sense so it returns empty list
print(strawhats[-5:-1]) #python reads this as: [(len(strawhats)-5):(len(strawhats)-1)] = [(10-5):(10-1)] = [5:9] -> Chopper, ..., Brook
print()

#Methods in List
print(nakama)

#Adding elements:
nakama.append("Coby")
print("After append:", nakama)
nakama.extend(["Bon Clay", "Bartolomeo", "Yamato", "Boa Hancock"])
print("After extend:", nakama)
nakama.insert(1, "Vivi")
print("After insert:", nakama)

#Removing elements:
strawhats.remove("Usopp")
nakama.append("Sogeking")   #Sorry not sorry XP
marry = nakama.pop()        #Can put an index inside () to pop the element of that index, otherwise last element is popped by default
print("I ship Luffy with", marry, "<3")
print("After pop:", nakama)

#Looping through a list
print("\nTraversing characters of each member:")
for member in nakama:
    print(f"\nCharacters in {member}:")
    for char in member:
        print(char)

admirers = strawhats + nakama
print(admirers)

#Other methods in List:
epic_eps = [278, 1071, 37, 312, 483, 396, 405, 1015, 26, 377]
print("Length:", len(epic_eps))
print("Count of '500':", epic_eps.count(500))     #Total number of times an element occurs
print("Index of '483':", epic_eps.index(483))     #First occurrence of the element
epic_eps.sort()
print("Sorted ascending list:", epic_eps)
epic_eps.sort(reverse=True)
print("Sorted descending list:", epic_eps)
epic_eps.reverse()
print("Reversed list:", epic_eps)


temp_list = ["temporary", "data"]
# Copying lists
temp_copy = temp_list.copy()
print("\nCopied list:", temp_copy)
"""
CANNOT simply do this:
temp_copy = temp_list
Because this will simply create another reference point/instance of the same list
And any changes done in temp_copy would also be reflected in the original temp_list
Hence use the method copy().
"""

#Clearing list
temp_list.clear()
print("\nCleared list:", temp_list)

#List comprehension
print("\nList comprehension example:")
squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)


#That is all about Lists for now
#Thank you!