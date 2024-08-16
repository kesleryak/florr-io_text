import random

Petals = ["Common Light", "Common Light", "Common Light", "Common Light", "Common Light", "Unusual Light", "Unusual Light", "Unusual Light", "Unusual Light", "Rare Light", "Rare Light", "Rare Light", "Epic Light", "Epic Light", "Epic Light"]
craftRate = {
    "Common": 40,
    "Unusual": 30,
    "Rare": 20,
    "Epic": 10,
    "Legendary": 3,
    "Mythic": 2,
    "Ultra": 1
}
raritylist = ["Common", "Unusual", "Rare", "Epic", "Legendary", "Mythic", "Ultra", "Super"]
rarityId = {
    "Common": 1,
    "Unusual": 2,
    "Rare": 3,
    "Epic": 4,
    "Legendary": 5,
    "Mythic": 6,
    "Ultra": 7
}
counter = 0
petalCounter = 0
craftPetal = ""
listPetal = []
removedSlots = []

while True:
    for p in Petals:
        
        print(p)
    home = input("What is the petal you would use to craft?")
    for p in Petals:
        if p == home:
            counter += 1
    if counter >= 5:
        counter = 0
        petalCounter = 0
        for p in Petals:
            if p == home:
                removedSlots.append(counter)
                petalCounter += 1
                if petalCounter == 5:
                    break
            else:
                counter += 1
        print(removedSlots)
        for r in removedSlots:
            Petals.pop(r)
        
        listPetal = home.split()
        petalCounter = random.randint(1, 100)
        if petalCounter <= craftRate[listPetal[0]]:
            Petals.append(raritylist[rarityId[listPetal[0]]] + " " + listPetal[1])
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
    listPetal = []
    removedSlots = []
