

#All variables here
home = ""
level = 1
playerHealth = 0
playerMaxHealth = 100

# start of code
while True:
    if playerHealth <= 0:
        playerHealth = playerMaxHealth
        home = input("Welcome to florr.io (text)! Press the following numbers to proceed. \n1: Play Game \n2: Instructions \n>")
    if home == "1":
        print('1')
