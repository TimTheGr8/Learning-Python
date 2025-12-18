import machine
import art

def ProcessCoins(money):
    total = 0
    for i in range(0, len(money)):
        if i == 0:
            change = 0.25
        elif i == 1:
            change = 0.1
        elif i == 2:
            change = 0.05
        elif i == 3:
            change = 0.01
        total += (money[i] * change)
    return total

def CollectMoney(money):
    money.clear()
    print("Enter the number of coins you will be using.")
    quarters = int(input("Number of quarters: "))
    money.append(quarters)
    dimes = int(input("Number if dimes: "))
    money.append(dimes)
    nickles = int(input("Number if nickles: "))
    money.append(nickles)
    pennies = int(input("Number if pennies: "))
    money.append(pennies)

def CheckResources(drink):
    ingredients = machine.MENU[drink]["ingredients"]

    for i in ingredients:
        if ingredients[i] <= machine.resources[i]:
            continue
        else:
            print("There are not enough ingredients for that drink")
            return False
    return True

def MakeDrink(drink):
    ingredients = machine.MENU[drink]["ingredients"]
    for i in ingredients:
        machine.resources[i] -= ingredients[i]
    machine.resources["money"] += machine.MENU[drink]["cost"]
    print("\n")
    print(art.coffee)
    print(f"Enjoy your {drink}!")

def GetPrice(drink):
    return machine.MENU[drink]["cost"]

def PrintReport():
    print(f"Machine Report:\nWater: {machine.resources["water"]}\nMilk: {machine.resources["milk"]}\nCoffee: {machine.resources["coffee"]}\nMoney: {machine.resources["money"]}")

def CheckInput(input, money):
    match input:
        case "off":
            print("Powering Down")
            return False
        case "report":
            PrintReport()
        case "espresso" | "latte" | "cappuccino":
            if CheckResources(input):
                price = GetPrice(input)
                print(f"Drink Price: {price: .2f}")
                CollectMoney(money)
                moneyCollected = ProcessCoins(money)
                if moneyCollected >= price:
                    if moneyCollected > price:
                        change = moneyCollected - price
                        print(f"Your change returned is {change: .2f}")
                    MakeDrink(input)
                else:
                    print("You did not add enough money. You change has been returned")
                    money.clear()
                    return False
        case _:
            print("I am sorry, that request is not valid. Pleases try again.")
    return True

def StartMachine():
    machineOn = True
    inputs = ["espresso", "latte", "cappuccino", "off", "report"]
    coins = []

    while machineOn:
        userInput = ""
        while userInput not in inputs:
            userInput = input("Today we have espresso, latte, and cappuccino. What drink would you like?\n").lower()
        
        machineOn = CheckInput(userInput, coins)

        if machineOn:
            anotherDrink = input("Would you like another drink?\nY or N: ").lower()
            if anotherDrink == "y":
                coins.clear()
                continue
            else:
                machineOn = False


# TODO 7: Make coffee

StartMachine()