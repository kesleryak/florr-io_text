home = ""
def area(num):
    if num == 1:
        home = input("You spawn in Centralia Fields 1. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n4: Go left \n5: Go right \n>")
        if home == "1":
            print("You went to hunt in CF1")
        elif home == "2":
            area(2)
        elif home == "3":
            area(9)
        elif home == "4":
            area(3)
        elif home == "5":
            area(5)
            
    elif num == 2:
        home = input("You went to Centralia. What would you do? \n1: Hunt \n2: Go left \n3: Go down \n>")
        if home == "1":
            print("You went to hunt in Centralia")
        elif home == "2":
            area(4)
        elif home == "3":
            area(1)
            
    elif num == 3:
        home = input("You went to Centralia Fields 2. What would you do? \n1: Hunt \n2: Go left \n3: Go right \n>")
        if home == "1":
            print("You went to hunt in CF2")
        elif home == "2":
            area(6)
        elif home == "3":
            area(1)
            
    elif num == 4:
        home = input("You went to Centralia Fields 3. What would you do? \n1: Hunt \n2: Go down-left \n3: Go up-left \n4: Go up \n5: Go right \n>")
        if home == "1":
            print("You went to hunt in CF3")
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
            print("You went to hunt in CF4")
        elif home == "2":
            area(1)
        elif home == "3":
            area(15)
        elif home == "4":
            area(14)

    elif num == 6:
        home = input("You went to Centralia Fields 5. What would you do? \n1: Hunt \n2: Go up \n3: Go up-right \n4: Go middle-right \n5: Go down-right \n>")
        if home == "1":
            print("You went to hunt in CF5")
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
            print("You went to hunt in CF6")
        elif home == "2":
            area(6)
        elif home == "3":
            area(8)

    elif num == 8:
        home = input("You went to Centralia Fields 7. What would you do? \n1: Hunt \n2: Go down \n3: Go left \n>")
        if home == "1":
            print("You went to hunt in CF7")
        elif home == "2":
            area(4)
        elif home == "3":
            area(7)

    elif num == 9:
        home = input("You went to South Desert 1. What would you do? \n1: Hunt \n2: Go up-left \n3: Go up-right \n4: Go down-left \n5: Go down-right \n>")
        if home == "1":
            print("You went to hunt in SD1")
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
            print("You went to hunt in SD2")
        elif home == "2":
            area(12)
        elif home == "3":
            area(9)

    elif num == 11:
        home = input("You went to South Desert 3. What would you do? \n1: Hunt \n2: Go up \n3: Go right \n>")
        if home == "1":
            print("You went to hunt in SD3")
        elif home == "2":
            area(9)
        elif home == "3":
            area(27)

    elif num == 12:
        home = input("You went to South Desert 4. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n>")
        if home == "1":
            print("You went to hunt in SD4")
        elif home == "2":
            area(13)
        elif home == "3":
            area(10)

    elif num == 13:
        home = input("You went to South Desert 5. What would you do? \n1: Hunt \n2: Go down \n3: Go right \n>")
        if home == "1":
            print("You went to hunt in SD5")
        elif home == "2":
            area(12)
        elif home == "3":
            area(9)

    elif num == 14:
        home = input("You went to Ellne Pass. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n>")
        if home == "1":
            print("You went to hunt in EP")
        elif home == "2":
            area(5)
        elif home == "3":
            area(28)

    elif num == 15:
        home = input("You went to Centralia Beach. What would you do? \n1: Hunt \n2: Go left \n3: Go up-right \n4: Go down-right \n>")
        if home == "1":
            print("You went to hunt in CB")
        elif home == "2":
            area(5)
        elif home == "3":
            area(16)
        elif home == "4":
            area(17)

    elif num == 16:
        home = input("You went to East Waters 1. What would you do? \n1: Hunt \n2: Go up \n3: Go left \n>")
        if home == "1":
            print("You went to hunt in EW1")
        elif home == "2":
            area(20)
        elif home == "3":
            area(15)

    elif num == 17:
        home = input("You went to East Waters 2. What would you do? \n1: Hunt \n2: Go left \n3: Go up-right \n4: Go down-right \n>")
        if home == "1":
            print("You went to hunt in EW2")
        elif home == "2":
            area(15)
        elif home == "3":
            area(18)
        elif home == "4":
            area(19)

    elif num == 18:
        home = input("You went to East Waters 3. What would you do? \n1: Hunt \n2: Go up into one of the 5 openings \n3: Go left \n4: Go down \n>")
        if home == "1":
            print("You went to hunt in EW3")
        elif home == "2":
            area(21)
        elif home == "3":
            area(17)
        elif home == "4":
            area(23)

    elif num == 19:
        home = input("You went to East Waters 4. What would you do? \n1: Hunt \n2: Go up \n3: Go right \n>")
        if home == "1":
            print("You went to hunt in EW4")
        elif home == "2":
            area(17)
        elif home == "3":
            area(22)

    elif num == 20:
        home = input("You went to Crab Kingdom. What would you do? \n1: Hunt \n2: Go down \n>")
        if home == "1":
            print("You went to hunt in CK")
        elif home == "2":
            area(16)

    elif num == 21:
        home = input("You went to Jellyfish Fields. What would you do? \n1: Hunt \n2: Go down into one of the 5 openings\n>")
        if home == "1":
            print("You went to hunt in JF")
        elif home == "2":
            area(18)

    elif num == 22:
        home = input("You went to Leech Zone. What would you do? \n1: Hunt \n2: Go left \n3: Go up \n4: Go down \n>")
        if home == "1":
            print("You went to hunt in LZ")
        elif home == "2":
            area(19)
        elif home == "3":
            area(23)
        elif home == "4":
            area(28)

    elif num == 23:
        home = input("You went to Starfish Zone. What would you do? \n1: Hunt \n2: Go up \n3: Go down \n>")
        if home == "1":
            print("You went to hunt in SZ")
        elif home == "2":
            area(18)
        elif home == "3":
            area(22)

    elif num == 24:
        home = input("You went to Ellne. What would you do? \n1: Hunt \n2: Go up \n>")
        if home == "1":
            print("You went to hunt in Ellne")
        elif home == "2":
            area(25)

    elif num == 25:
        home = input("You went to Ellne Jungle 1. What would you do? \n1: Hunt \n2: Go left \n3: Go up \n4: Go down \n>")
        if home == "1":
            print("You went to hunt in EJ1")
        elif home == "2":
            area(26)
        elif home == "3":
            area(29)
        elif home == "4":
            area(24)

    elif num == 26:
        home = input("You went to Ellne Jungle 2. What would you do? \n1: Hunt \n2: Go left \n3: Go right \n4: Go up \n>")
        if home == "1":
            print("You went to hunt in EJ2")
        elif home == "2":
            area(27)
        elif home == "3":
            area(25)
        elif home == "4":
            area(28)

    elif num == 27:
        home = input("You went to Ellne Jungle 3. What would you do? \n1: Hunt \n2: Go up \n3: Go left \n4: Go right \n>")
        if home == "1":
            print("You went to hunt in EJ3")
        elif home == "2":
            area(28)
        elif home == "3":
            area(11)
        elif home == "4":
            area(26)

    elif num == 28:
        home = input("You went to Ellne Jungle 4. What would you do? \n1: Hunt \n2: Go up-left \n3: Go up-right \n4: Go down-left \n5: Go down-right \n6: Go right \n>")
        if home == "1":
            print("You went to hunt in EJ4")
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
            print("You went to hunt in EJ1")
        elif home == "2":
            area(28)
        elif home == "3":
            area(25)

while True:
    area(1)
