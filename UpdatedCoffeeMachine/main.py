from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

machineOn = True
while machineOn:
    userInput = input(f"What would you like to order? We have {menu.get_items()} \n").lower()
    if userInput == "report":
        machine.report()
    elif userInput == "off":
        machineOn = False
    elif menu.find_drink(userInput):
        drink = menu.find_drink(userInput)
        print(f"Your total is: {drink.cost}")
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(drink)
