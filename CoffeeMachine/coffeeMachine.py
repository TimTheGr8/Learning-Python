import machine


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

    print(f"Total: {total: .2f}")

def CheckResources(drink):
    pass

def MakeDrink(drink, money):
    print("Enter the number of coins you will be using.")
    quarters = int(input("Number of quarters: "))
    money.append(quarters)
    dimes = int(input("Number if dimes: "))
    money.append(dimes)
    nickles = int(input("Number if nickles: "))
    money.append(nickles)
    pennies = int(input("Number if pennies: "))
    money.append(pennies)
    ProcessCoins(money)
    print(f"Here is your {drink}!")

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
            MakeDrink(input, money)
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
        # Move this so that it only gets called when the user inputs a proper drink
        
        machineOn = CheckInput(userInput, coins)

        if machineOn:
            anotherDrink = input("Would you like another drink?\nY or N: ").lower()
            if anotherDrink == "y":
                coins.clear()
                continue
            else:
                machineOn = False

# TODO 4: Check if resources are sufficient to make selected drink



# TODO 5: Process coins - 



# TODO 6: Check if the transaction is sucessful



# TODO 7: Make coffee

StartMachine()