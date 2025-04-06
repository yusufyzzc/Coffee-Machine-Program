from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the classes
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


# Initialize the coffee machine
is_on = True
while is_on:
    choice = input(f"what would u like to drink? ({menu.get_items()}) ")
    if choice == "off":
        is_on == False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        