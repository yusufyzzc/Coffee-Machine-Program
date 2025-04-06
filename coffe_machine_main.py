import os
import menu
from menu import MENU, resources, profit


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coffee_machine():
    global resources, profit
    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
            continue
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            try:
                print(f"Please insert coins.")
                quarters = int(input("How many quarters? ")) * 0.25
                dimes = int(input("How many dimes? ")) * 0.10
                nickels = int(input("How many nickels? ")) * 0.05
                pennies = int(input("How many pennies? ")) * 0.01
                total = quarters + dimes + nickels + pennies
                print(f"Total: ${total}")
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if total < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif total >= drink["cost"]:
                change = total - drink["cost"]
                print(f"Here is ${change:.2f} in change.")
                profit += drink["cost"]
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                
            ingredients = MENU[choice]["ingredients"]
            for item in ingredients:
                resources[item] -= ingredients[item]
                print(f"{item.capitalize()} used: {ingredients[item]}")
            print(f"Here is your {choice} ☕. Enjoy!")

if __name__ == "__main__":
    coffee_machine()

        