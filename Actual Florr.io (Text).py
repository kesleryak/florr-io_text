import random

#All variables here
home = ""
rarity = 0
raritylist = ["Common", "Unusual", "Rare", "Epic", "Legendary", "Mythic", "Ultra", "Super"]
mob = 0
moblist = ["Ant", "Ladybug", "Bee", "Rock", "Hornet", "Dandelion", "Ant Egg", "Cactus", "Sandstorm", "Beetle", "Fire Ant", "Fire Ant Egg", "Leech", "Sponge", "Jellyfish", "Starfish", "Crab", "Bubble", "Bush", "Dark Ladybug", "Leafbug", "Mantis", "Wasp", "Termite"]
mobHealth = 0
mobDamage = 0
allMobHealth = {
    "Ant": 25,
    "Ladybug": 62,
    "Bee": 37,
    "Rock": 100,
    "Hornet": 62,
    "Dandelion": 25,
    "Ant Egg": 150,
    "Cactus": 75,
    "Beetle": 100,
    "Sandstorm": 125,
    "Fire Ant": 31,
    "Fire Ant Egg": 150,
    "Jellyfish": 125,
    "Leech": 175,
    "Starfish": 150,
    "Crab": 150,
    "Sponge": 100,
    "Bubble": 1,
    "Bush": 25,
    "Dark Ladybug": 87,
    "Leafbug": 50,
    "Mantis": 100,
    "Wasp": 62,
    "Termite": 50
}
rarityId = {
    "Common": 1,
    "Unusual": 2,
    "Rare": 3,
    "Epic": 4,
    "Legendary": 5,
    "Mythic": 6,
    "Ultra": 7,
    "Super": 8
}
allMobDamage = {
    "Ant": 10,
    "Ladybug": 10,
    "Bee": 50,
    "Rock": 10,
    "Hornet": 50,
    "Dandelion": 15,
    "Ant Egg": 3,
    "Cactus": 5,
    "Beetle": 30,
    "Sandstorm": 40,
    "Fire Ant": 20,
    "Fire Ant Egg": 3,
    "Jellyfish": 25,
    "Leech": 10,
    "Starfish": 20,
    "Crab": 25,
    "Sponge": 10,
    "Bubble": 5,
    "Bush": 10,
    "Dark Ladybug": 10,
    "Leafbug": 30,
    "Mantis": 20,
    "Wasp": 50,
    "Termite": 10
}
allPetals = ["Leaf", "Rose", "Stinger", "Rock", "Missile", "Dandelion", "Ant Egg", "Cactus", "Sand", "Beetle Egg", "Yucca", "Ant Egg", "Fangs", "Sponge", "Lightning", "Starfish", "Claw", "Bubble", "Cotton", "Dahila", "Root", "Peas", "Bloodstinger", "Carrot"]
allPetalDamage = {
    "Leaf": 0,
    "Rose": 0,
    "Stinger": 100,
    "Rock": 15,
    "Missile": 25,
    "Dandelion": 5,
    "Ant Egg": 10,
    "Cactus": 5,
    "Beetle Egg": 30,
    "Sand": 20,
    "Yucca": 0,
    "Ant Egg": 10,
    "Lightning": 12,
    "Claw": 5,
    "Sponge": 0,
    "Bubble": 0,
    "Cotton": 0,
    "Dahila": 0,
    "Root": 5,
    "Peas": 32,
    "Bloodstinger": 100,
    "Carrot": 10,
    "Basic": 10
    
}
allPetalHeal = {
    "Leaf": 3,
    "Rose": 7,
    "Stinger": 0,
    "Rock": 0,
    "Missile": 0,
    "Dandelion": 0,
    "Ant Egg": 0,
    "Cactus": 0,
    "Beetle Egg": 0,
    "Sand": 0,
    "Yucca": 4,
    "Ant Egg": 0,
    "Lightning": 0,
    "Claw": 0,
    "Sponge": 0,
    "Bubble": 0,
    "Cotton": 0,
    "Dahila": 11,
    "Root": 0,
    "Peas": 0,
    "Bloodstinger": -5,
    "Carrot": 0,
    "Basic": 0
    
}
global playerHealth
global playerMaxHealth
playerHealth = 0
playerMaxHealth = 100
playerAttack = 50
petal = ""
global listText
listText = []
global counter
counter = 0
global Exp  
Exp = 0
global maxExp
maxExp = 100
playerPetals = ["Common Basic", "Common Basic", "Common Basic", "Common Basic", "Common Basic"]
global invPetals
invPetals = []
equippingPetal = ""
removedPetal = ""
craftRate = {
    "Common": 40,
    "Unusual": 30,
    "Rare": 20,
    "Epic": 10,
    "Legendary": 3,
    "Mythic": 2,
    "Ultra": 1
}
petalCounter = 0
craftPetal = ""
removedSlots = []
global playerHeal
playerHeal = 0
global level
level = 1


def crafting():
    global counter
    global petalCounter
    global craftPetal
    global listText
    global removedSlots
    global invPetals
    for p in invPetals:
        print(p)
    home = input("What is the petal you would use to craft?")
    for p in invPetals:
        if p == home:
            counter += 1
    if counter >= 5:
        counter = 0
        petalCounter = 0
        for p in invPetals:
            if p == home:
                removedSlots.append(counter)
                petalCounter += 1
                if petalCounter == 5:
                    break
            else:
                counter += 1
        print(removedSlots)
        for r in removedSlots:
            invPetals.pop(r)
        
        listText = home.split()
        petalCounter = random.randint(1, 100)
        if petalCounter <= craftRate[listText[0]]:
            invPetals.append(raritylist[rarityId[listText[0]]] + " " + listText[1])
            print(petalCounter)
            print("Crafting succesful")
            print("----------------------------------------")
        else:
            print(petalCounter)
            print("Crafting unsucessful")
            print("----------------------------------------")
        
    counter = 0
    petalCounter = 0
    craftPetal = ""
    listText = []
    removedSlots = []


def equip():
    global invPetals
    global playerAttack
    global equippingPetal
    global playerHeal
    for p in invPetals:
        print(p)
    home = input("Which petal do you want to equip?")
    for p in invPetals:
        if p == home:
            equippingPetal = p
            invPetals.remove(p)
            break
    for p in playerPetals:
        global counter
        print(counter, p)
        counter += 1
    counter = 0
    home = input("Which slot do you want to replace your selected petal? Type the petal slot number.")
    removedPetal = playerPetals[int(home)]
    playerPetals.pop(int(home))
    playerPetals.insert(int(home), equippingPetal)
    invPetals.append(removedPetal)
    print("New equipped petals:")
    for p in playerPetals:
        print(p)
    print("New Damage:")
    playerAttack = 0
    for p in playerPetals:
        listText = p.split()
        playerAttack += (allPetalDamage[listText[1]] * (3 ** (rarityId[listText[0]]-1)))
    print(playerAttack)
    listText = []
    print("New Heal Rate:")
    playerHeal = 0
    for p in playerPetals:
        listText = p.split()
        playerHeal += ((allPetalHeal[listText[1]] * (3 ** (rarityId[listText[0]]-1))))
    print(playerHeal)
    listText = []
    print("---------------------------------------------------------")


def absorb():
    global counter
    counter = 1
    global invPetals
    global maxExp
    global level
    global playerMaxHealth
    for p in invPetals:
        print(p)
    home = input("What do you want to absorb?")
    if home != "Nothing":
        for p in invPetals:
            if p == home:
                global listText
                listText = p.split()
                invPetals.remove(p)
                break
        for r in raritylist:
            if r == listText[0]:
                global Exp
                Exp += counter
                break
            else:
                counter *= 10
    counter = 0
    listText = []
    while Exp >= maxExp:
        Exp -= maxExp
        maxExp += 100
        level += 1
        playerMaxHealth += 100




def hunting(num):
    global playerHealth
    global playerMaxHealth
    global rarity
    global level
    global Exp
    global maxExp 
    while playerHealth > 0:
        if num == 1:
            mob = random.randint(0, 3)
            rarity = random.randint(0, 1)
        elif num == 2:
            mob = random.randint(0, 1)
            rarity = random.randint(0, 1)
        elif num == 3:
            mob = random.randint(1, 3)
            rarity = random.randint(0, 2)
        elif num == 4:
            mob = random.randint(0, 3)
            rarity = random.randint(1, 3)
        elif num == 5:
            mob = 16
            rarity = random.randint(0, 2)
        elif num == 6:
            mob = random.randint(0, 4)
            rarity = random.randint(2, 3)
        elif num == 7:
            mob = random.randint(0, 4)
            rarity = random.randint(3, 5)
        elif num == 8:
            mob = random.randint(4, 5)
            rarity = random.randint(2, 4)
        elif num == 9:
            mob = random.randint(7, 9)
            rarity = random.randint(0, 2)
        elif num == 10:
            mob = random.randint(8, 9)
            rarity = random.randint(2, 3)
        elif num == 11:
            mob = random.randint(7, 8)
            rarity = random.randint(2, 4)
        elif num == 12:
            mob = random.randint(7, 9)
            rarity = random.randint(2, 4)
        elif num == 13:
            mob = random.randint(7, 9)
            rarity = random.randint(3, 5)
        elif num == 14:
            mob = 16
            rarity = random.randint(1, 3)
        elif num == 15:
            mob = random.randint(15, 17)
            rarity = random.randint(0, 2)
        elif num == 16:
            mob = random.randint(15, 17)
            rarity = random.randint(1, 3)
        elif num == 17:
            mob = random.randint(13, 14)
            rarity = random.randint(2, 3)
        elif num == 18:
            mob = random.randint(13, 17)
            rarity = random.randint(3, 4)
        elif num == 19:
            mob = random.randint(15, 17)
            rarity = random.randint(3, 4)
        elif num == 20:
            mob = random.randint(16, 17)
            rarity = random.randint(4, 5)
        elif num == 21:
            mob = 14
            rarity = 5
        elif num == 22:
            mob = 12
            rarity = random.randint(3, 4)
        elif num == 23:
            mob = 15
            rarity = random.randint(4, 5)
        elif num == 24:
            mob = 18
            rarity = 0
        elif num == 25:
            mob = random.randint(18, 22)
            rarity = random.randint(0, 1)
        elif num == 26:
            mob = random.randint(18, 22)
            rarity = random.randint(2, 3)
        elif num == 27:
            mob = random.randint(18, 22)
            rarity = random.randint(2, 3)
        elif num == 28:
            mob = random.randint(18, 22)
            rarity = random.randint(3, 4)
        elif num == 29:
            mob = random.randint(18, 22)
            rarity = random.randint(4, 5)
        mobHealth = allMobHealth[moblist[mob]] * (5 ** rarity)
        home = print("You met a", raritylist[rarity], moblist[mob])
        while mobHealth > 0:
            home = print("Your health:", playerHealth, "/", playerMaxHealth)
            home = print("Mob Health:", mobHealth)
            home = input("What would you do? \n1: Attack \n2: Run away \n>")
            if home == "1":
                home = print("You dealt", playerAttack, "damage.")
                mobHealth -= playerAttack
                if mobHealth > 0:
                    mobDamage = allMobDamage[moblist[mob]] * (3 ** rarity)
                    home = print("The", moblist[mob], "dealt", mobDamage, "damage to you.")
                    playerHealth -= mobDamage
                    if playerHealth <= 0:
                        home = print("You died.")
                        break
                if playerHealth != playerMaxHealth:
                    print("You healed", playerHeal, "health.")
                    playerHealth += playerHeal
                    if playerHealth > playerMaxHealth:
                        playerHealth = playerMaxHealth
            if home == "2":
                break
        if home == "2":
            break
        if mobHealth <= 0:
                home = print("You gained a", raritylist[rarity], allPetals[mob])
                petal = raritylist[rarity] + " " + allPetals[mob]
                invPetals.append(petal)




def area(num):
    # all maps of players, test of recursion
    if num == 1:
        global playerHealth
        global playerMaxHealth
        global rarity
        global level
        global Exp
        global maxExp 
        home = print("Level:", level)
        home = print("Exp:", Exp, "/", maxExp)
        home = print("Your health:", playerHealth, "/", playerMaxHealth)
        home = input("You spawn in Centralia Fields 1. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n4: Go left \n5: Go right \n>")
        if home == "1":
            hunting(1)
        elif home == "2":
            area(2)
        elif home == "3":
            area(9)
        elif home == "4":
            area(3)
        elif home == "5":
            area(5)
        elif home == "abs":
            absorb()
            area(1)
        elif home == "equ":
            equip()
            area(1)
        elif home == "cra":
            crafting()
            area(1)
            
    elif num == 2:
        home = print("Your health:", playerHealth, "/", playerMaxHealth)
        home = input("You went to Centralia. What would you do? \n1: Hunt \n2: Go left \n3: Go down \n>")
        if home == "1":
            hunting(2)
        elif home == "2":
            area(4)
        elif home == "3":
            area(1)
            
    elif num == 3:
        home = input("You went to Centralia Fields 2. What would you do? \n1: Hunt \n2: Go left \n3: Go right \n>")
        if home == "1":
            hunting(3)
        elif home == "2":
            area(6)
        elif home == "3":
            area(1)
            
    elif num == 4:
        home = input("You went to Centralia Fields 3. What would you do? \n1: Hunt \n2: Go down-left \n3: Go up-left \n4: Go up \n5: Go right \n>")
        if home == "1":
            hunting(4)
        elif home == "2":
            area(6)
        elif home == "3":
            area(6)
        elif home == "4":
            area(8)
        elif home == "5":
            area(2)

    elif num == 5:
        home = input("You went to Centralia Fields 4. What would you do? \n1: Hunt \n2: Go left \n3: Go right \n4: Go down \n>")
        if home == "1":
            hunting(5)
        elif home == "2":
            area(1)
        elif home == "3":
            area(15)
        elif home == "4":
            area(14)

    elif num == 6:
        home = input("You went to Centralia Fields 5. What would you do? \n1: Hunt \n2: Go up \n3: Go up-right \n4: Go middle-right \n5: Go down-right \n>")
        if home == "1":
            hunting(6)
        elif home == "2":
            area(7)
        elif home == "3":
            area(4)
        elif home == "4":
            area(4)
        elif home == "5":
            area(3)

    elif num == 7:
        home = input("You went to Centralia Fields 6. What would you do? \n1: Hunt \n2: Go down \n3: Go right \n>")
        if home == "1":
            hunting(7)
        elif home == "2":
            area(6)
        elif home == "3":
            area(8)

    elif num == 8:
        home = input("You went to Centralia Fields 7. What would you do? \n1: Hunt \n2: Go down \n3: Go left \n>")
        if home == "1":
            hunting(8)
        elif home == "2":
            area(4)
        elif home == "3":
            area(7)

    elif num == 9:
        home = print("Your health:", playerHealth, "/", playerMaxHealth)
        home = input("You went to South Desert 1. What would you do? \n1: Hunt \n2: Go up-left \n3: Go up-right \n4: Go down-left \n5: Go down-right \n>")
        if home == "1":
            hunting(9)
        elif home == "2":
            area(13)
        elif home == "3":
            area(1)
        elif home == "4":
            area(10)
        elif home == "5":
            area(11)

    elif num == 10:
        home = input("You went to South Desert 2. What would you do? \n1: Hunt \n2: Go up-left \n3: Go up-right \n>")
        if home == "1":
            hunting(10)
        elif home == "2":
            area(12)
        elif home == "3":
            area(9)

    elif num == 11:
        home = input("You went to South Desert 3. What would you do? \n1: Hunt \n2: Go up \n3: Go right \n>")
        if home == "1":
            hunting(11)
        elif home == "2":
            area(9)
        elif home == "3":
            area(27)

    elif num == 12:
        home = input("You went to South Desert 4. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n>")
        if home == "1":
            hunting(12)
        elif home == "2":
            area(13)
        elif home == "3":
            area(10)

    elif num == 13:
        home = input("You went to South Desert 5. What would you do? \n1: Hunt \n2: Go down \n3: Go right \n>")
        if home == "1":
            hunting(13)
        elif home == "2":
            area(12)
        elif home == "3":
            area(9)

    elif num == 14:
        home = input("You went to Ellne Pass. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n>")
        if home == "1":
            hunting(14)
        elif home == "2":
            area(5)
        elif home == "3":
            area(28)

    elif num == 15:
        home = input("You went to Centralia Beach. What would you do? \n1: Hunt \n2: Go left \n3: Go up-right \n4: Go down-right \n>")
        if home == "1":
            hunting(15)
        elif home == "2":
            area(5)
        elif home == "3":
            area(16)
        elif home == "4":
            area(17)

    elif num == 16:
        home = input("You went to East Waters 1. What would you do? \n1: Hunt \n2: Go up \n3: Go left \n>")
        if home == "1":
            hunting(16)
        elif home == "2":
            area(20)
        elif home == "3":
            area(15)

    elif num == 17:
        home = input("You went to East Waters 2. What would you do? \n1: Hunt \n2: Go left \n3: Go up-right \n4: Go down-right \n>")
        if home == "1":
            hunting(17)
        elif home == "2":
            area(15)
        elif home == "3":
            area(18)
        elif home == "4":
            area(19)

    elif num == 18:
        home = input("You went to East Waters 3. What would you do? \n1: Hunt \n2: Go up into one of the 5 openings \n3: Go left \n4: Go down \n>")
        if home == "1":
            hunting(18)
        elif home == "2":
            area(21)
        elif home == "3":
            area(17)
        elif home == "4":
            area(23)

    elif num == 19:
        home = input("You went to East Waters 4. What would you do? \n1: Hunt \n2: Go up \n3: Go right \n>")
        if home == "1":
            hunting(19)
        elif home == "2":
            area(17)
        elif home == "3":
            area(22)

    elif num == 20:
        home = input("You went to Crab Kingdom. What would you do? \n1: Hunt \n2: Go down \n>")
        if home == "1":
            hunting(20)
        elif home == "2":
            area(16)

    elif num == 21:
        home = input("You went to Jellyfish Fields. What would you do? \n1: Hunt \n2: Go down into one of the 5 openings\n>")
        if home == "1":
            hunting(21)
        elif home == "2":
            area(18)

    elif num == 22:
        home = input("You went to Leech Zone. What would you do? \n1: Hunt \n2: Go left \n3: Go up \n4: Go down \n>")
        if home == "1":
            hunting(22)
        elif home == "2":
            area(19)
        elif home == "3":
            area(23)
        elif home == "4":
            area(28)

    elif num == 23:
        home = input("You went to Starfish Zone. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n>")
        if home == "1":
            hunting(23)
        elif home == "2":
            area(18)
        elif home == "3":
            area(22)

    elif num == 24:
        home = input("You went to Ellne. What would you do? \n1: Hunt \n2: Go up \n>")
        if home == "1":
            hunting(24)
        elif home == "2":
            area(25)

    elif num == 25:
        home = input("You went to Ellne Jungle 1. What would you do? \n1: Hunt \n2: Go left \n3: Go up \n4: Go down \n>")
        if home == "1":
            hunting(25)
        elif home == "2":
            area(26)
        elif home == "3":
            area(29)
        elif home == "4":
            area(24)

    elif num == 26:
        home = input("You went to Ellne Jungle 2. What would you do? \n1: Hunt \n2: Go left \n3: Go right \n4: Go up \n>")
        if home == "1":
            hunting(26)
        elif home == "2":
            area(27)
        elif home == "3":
            area(25)
        elif home == "4":
            area(28)

    elif num == 27:
        home = input("You went to Ellne Jungle 3. What would you do? \n1: Hunt \n2: Go up \n3: Go left \n4: Go right \n>")
        if home == "1":
            hunting(27)
        elif home == "2":
            area(28)
        elif home == "3":
            area(11)
        elif home == "4":
            area(26)

    elif num == 28:
        home = input("You went to Ellne Jungle 4. What would you do? \n1: Hunt \n2: Go up-left \n3: Go up-right \n4: Go down-left \n5: Go down-right \n6: Go right \n>")
        if home == "1":
            hunting(28)
        elif home == "2":
            area(14)
        elif home == "3":
            area(22)
        elif home == "4":
            area(27)
        elif home == "5":
            area(26)
        elif home == "6":
            area(29)

    elif num == 29:
        home = input("You went to Ellne Jungle 5. What would you do? \n1: Hunt \n2: Go left \n3: Go down \n>")
        if home == "1":
            hunting(29)
        elif home == "2":
            area(28)
        elif home == "3":
            area(25)

# start of code
while True:
    if playerHealth <= 0:
        playerHealth = playerMaxHealth
        home = input("Welcome to florr.io (text)! Press the following numbers to proceed. \n1: Play Game \n2: Instructions \n>")
    if home == "1":
        area(1)
