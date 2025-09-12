#Functions in Python:
#P.s.: I play Genshin Impact so I though why not do a little collaboration with Python XP


# 1. Simple function (no parameters, no return value)
def greet_traveler():
    print("Hello, Traveler! Welcome to Teyvat.")

# 2. Function with parameters (positional arguments)
def attack(character, damage):
    return f"{character} deals {damage} DMG!"

# 3. Function with default arguments
def elemental_skill(character, element="Anemo"):
    return f"{character} uses their {element} skill!"

# 4. Function with keyword arguments
def introduce_character(name, vision, region):
    print(f"I am {name}, a {vision} user from {region}.")

# 5. Function with variable-length arguments (*args)
def party_setup(*characters):
    print("Your party members are:")
    for char in characters:
        print("-", char)

# 6. Function with keyword variable-length arguments (**kwargs)
def character_stats(**stats):
    print("Character Stats:")
    for key, value in stats.items():
        print(f"{key} : {value}")

# 7. Recursive function (calculate factorial-like 'Ascension Material Requirement')
def ascension_materials(level):
    if level == 1:
        return 1
    return level * ascension_materials(level-1)

# 8. Lambda function (quick elemental burst damage calculation)
burst_damage = lambda atk, multiplier: atk * multiplier


# ---------------- Main Program Execution ----------------

print("1. Simple Function:")
greet_traveler()

print("\n2. Function with Parameters and Return Value:")
print(attack("Diluc", 5000))

print("\n3. Function with Default Arguments:")
print(elemental_skill("Venti"))
print(elemental_skill("Hu Tao", "Pyro"))

print("\n4. Function with Keyword Arguments:")
introduce_character(region="Mondstadt", name="Jean", vision="Anemo")

print("\n5. Function with *args (Party Setup):")
party_setup("Xiao", "Zhongli", "Albedo", "Ganyu")

print("\n6. Function with **kwargs (Character Stats):")
character_stats(Name="Raiden Shogun", Vision="Electro", Weapon="Polearm", Region="Inazuma")

print("\n7. Recursive Function (Ascension Material Requirement):")
print("Materials needed up to level 5 =", ascension_materials(5))

print("\n8. Lambda Function:")
print("Kazuha's Burst Damage =", burst_damage(1200, 4.2))
