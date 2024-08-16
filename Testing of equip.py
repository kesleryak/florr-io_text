playerPetals = ["Common Basic", "Common Basic", "Common Basic", "Common Basic", "Common Basic"]
invPetals = ["Common Light", "Common Light", "Common Light", "Common Light", "Common Light", "Unusual Light", "Unusual Light", "Unusual Light", "Rare Light", "Rare Light", "Rare Light", "Epic Light", "Epic Light", "Epic Light"]
equippingPetal = ""
removedPetal = ""
counter = 0


while True:
    #equip command
    for p in invPetals:
        print(p)
    home = input("Which petal do you want to equip?")
    for p in invPetals:
        if p == home:
            equippingPetal = p
            invPetals.remove(p)
            break
    for p in playerPetals:
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
    print("---------------------------------------------------------")
