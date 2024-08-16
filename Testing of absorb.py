Petals = ["Common Light", "Common Light", "Common Light", "Common Light", "Common Light", "Unusual Light", "Unusual Light", "Unusual Light", "Rare Light", "Rare Light", "Rare Light", "Epic Light", "Epic Light", "Epic Light"]
raritylist = ["Common", "Unusual", "Rare", "Epic", "Legendary", "Mythic", "Ultra", "Super"]
listText = []
counter = 1
Exp = 0

while True:
    #absorb function
    for p in Petals:
        print(p)
    home = input("What do you want to absorb?")
    for p in Petals:
        if p == home:
            listText = p.split()
            Petals.remove(p)
            break
    for r in raritylist:
        if r == listText[0]:
            Exp += counter
            break
        else:
            counter *= 5
    counter = 1
    print("Exp:", Exp)
            
