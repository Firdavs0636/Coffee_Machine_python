from resources import MENU, resources
from coins import coin


def coin_processor():
    """Takes input from a user and counts overall deposit"""
    alpha = 0
    for j in coin:
        deposit = int(input(f"How many {j}?: "))
        alpha += deposit * coin[j]
    return alpha


def resource_checker(ingredients):
    """Checks whether ingredients are enough or not"""
    for i in ingredients.keys():
        if resources[i] < ingredients[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def coffee_maker(profit):
    """Runs the machine as it goes ON"""
    money = 0
    choice = input("    Would you like: Espresso / Latte / Cappuccino: ").lower()
    if choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    elif choice == 'off':
        return
    else:
        drink = MENU[choice]
        if resource_checker(drink['ingredients']):
            print("Please insert coins")
            money += round(coin_processor(), 2)

#   to decrement values of ingredients
            for i in drink['ingredients'].keys():
                resources[i] -= drink['ingredients'][i]
            money -= drink['cost']
            profit += drink['cost']
            print(f"Here is ${round(money, 2)} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
            if money <= drink['cost']:
                print("Sorry there is not enough money. Money refunded.")
    coffee_maker(profit)


coffee_maker(0)
