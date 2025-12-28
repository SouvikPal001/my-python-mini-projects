#Tuples in Python
"""
A tuple is an ordered, immutable collection of items.
Once created, a tuple CANNOT be modified.
Tuples are slightly more memory-efficient than lists because tuples have a simpler internal structure than lists

We use tuples when:
- Data should not change
- We want safety from accidental modification
- We need faster access than lists

Tuple items are separated by commas and enclosed within (ROUND PARENTHESES).
The index of a tuple in Python starts from 0 and ends at n-1.
"""

#Basic tuple declaration
warlords = ("Dracule Mihawk", "Crocodile", "Donquixote Doflamingo", "Bartholomew Kuma", "Gecko Moria", "Boa Hancock", "Jimbei")
# Index:           [0]            [1]                [2]                   [3]               [4]            [5]          [6]
print(type(warlords))
# warlords[1] = "Sir Crocodile" ---> ERROR! Because Tuples are immutable and cannot be directly modified

# Tuple with mixed datatypes
warlord_details = ("Warlords of the Sea", 7, True, 3.59)

#Single-element tuple
unseen_warlord = ("Hanafuda",)

"""
NOTE(!IMP!):
("Hanafuda") -> NOT a tuple (it's a string)
(2010) -> Not a tuple (it's an int)
("Hanafuda",) -> tuple
COMMA makes the tuple, not the parentheses.
"""

# Looping through a tuple
print("\nTraversing the tuple:")
for warlord in warlords:
    print(warlord)

# Nested tuples
warlord_bounties = (
    ("Mihawk", 3590000000),
    ("Blackbeard", 3996000000),
    ("Doflamingo", 340000000),
)
print("\nNested tuple:")
for name, bounty in warlord_bounties:
    print(f"{name} has a bounty of {bounty}")

print("\nAccessing elements:")
print(warlords[0])    #First element -> Dracule Mihawk
print(warlords[1])    #Element present on the given index -> Crocodile
print(warlords[-1])   #Last element -> Jimbei
#How python interprets negative indexes(for easier understanding):
print(warlords[-4])    #Python reads this as warlords[len(warlords) - 4] = warlords[7 - 4] = warlords[3] -> Bartholomew Kuma
# print(warlords[10])   #Error: Index out of bound/Tuple index out of range
print()

#Tuple Slicing:
# NOTE: slicing always moves left → right
print(len(warlords)) #length of the tuple -> 7
print(warlords[0:3]) #including 0 but not 3 -> Dracule Mihawk, ..., Donquixote Doflamingo
print(warlords[1:3]) #including 1 but not 3 -> Crocodile, ..., Donquixote Doflamingo
print(warlords[:3])  #starting from 0 by default upto 3 but not including 3 -> Dracule Mihawk, ..., Donquixote Doflamingo
print(warlords[3:])  #including 3 upto len-1 -> Bartholomew Kuma, ..., Jimbei
print(warlords[:])   #traverses the whole tuple (creates a shallow copy), i.e, from 0 to len-1 -> Dracule Mihawk, ..., Jimbei
print(warlords[0:-4])  #python reads this as: [0:(len(warlords)-4)] = [0:(7-4)] = [0:3] -> Dracule Mihawk, ..., Donquixote Doflamingo
print(warlords[-1:-5]) #python reads this as: [(len(warlords)-1):(len(warlords)-5)] = [(7-1):(7-5)] = [6:2] which doesn't really make sense so it returns empty tuple
print(warlords[-5:-1]) #python reads this as: [(len(warlords)-5):(len(warlords)-1)] = [(7-5):(7-1)] = [2:6] -> Donquixote Doflamingo, ..., Boa Hancock
print()

#Tuple methods (very few compared to lists)
print("\nTuple methods:")
print("Length:", len(warlords))
print("Count of 'Jimbei':", warlords.count("Jimbei"))
print("Index of 'Boa Hancock':", warlords.index("Boa Hancock"))
#Also there is min, max and sum methods for comparable types like int, float, etc

#Converting tuple to list (when modification is needed)
print("\nConverting tuple to list:")
new_warlords = list(warlords)
new_warlords.remove("Crocodile")
new_warlords.remove("Gecko Moria")
new_warlords.pop(2)
new_warlords.pop()
new_warlords.append("Marshall D. Teach (Blackbeard)")
new_warlords.extend(["Trafalgar D. Water Law", "Buggy", "Edward Weevil"])
print(new_warlords)

#Converting back to tuple
print("\nConverted back to tuple:")
warlords = tuple(new_warlords)      #This creates a NEW tuple object in the memory, the variable name is reused, but the original tuple object still exists until garbage collected but it becomes unreachable
print(warlords)



#That is all about Tuples for now
#Thank you!