menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

reduced_resources = resources

insufficient_ingredients = False


def resource_reducer(drink_name, reduced_resources, drink_water, drink_milk, drink_coffee):
    reduced_resources['water'] = reduced_resources['water'] - drink_water
    if drink_name != 'espresso':
        reduced_resources['milk'] = reduced_resources['milk'] - drink_milk
    else:
        reduced_resources['milk'] = reduced_resources['milk']
    reduced_resources['coffee'] = reduced_resources['coffee'] - drink_coffee
    return reduced_resources


def has_enough_ingredients(reduced_resources, drink_water, drink_milk, drink_coffee):
    if reduced_resources['water'] < drink_water or  reduced_resources['milk'] < drink_milk or reduced_resources['coffee'] < drink_coffee:
        return 1
    elif drink_water == 0:
        return 2
    else:
        return 0


money_collected = 0

while not insufficient_ingredients:
    drink_name = input("What would you like? (espresso/latte/cappuccino): ")

    if drink_name == 'report' or drink_name == 'off':
        drink_cost = 0
        drink_water = 0
        drink_milk = 0
        drink_coffee = 0

    else:
        drink_cost = menu[drink_name]['cost']
        drink_water = menu[drink_name]['ingredients']['water']
        if drink_name != 'espresso':
            drink_milk = menu[drink_name]['ingredients']['milk']
        drink_coffee = menu[drink_name]['ingredients']['coffee']
        money_collected += drink_cost

    if drink_name == 'espresso':
        drink_milk = 0
        enough_ingredients = has_enough_ingredients(reduced_resources, drink_water, drink_milk, drink_coffee)
    elif drink_name == 'report':
        print(f"Water: {reduced_resources['water']}ml\nMilk: {reduced_resources['milk']}ml\nCoffee: {reduced_resources['coffee']}g\nMoney: ${money_collected}")
        insufficient_ingredients = False
        enough_ingredients = has_enough_ingredients(reduced_resources, drink_water, drink_milk, drink_coffee)
    elif drink_name == 'off':
        exit()
    else:
        enough_ingredients = has_enough_ingredients(reduced_resources, drink_water, drink_milk, drink_coffee)

    if enough_ingredients == 1:
        if drink_water < reduced_resources['water'] or reduced_resources['water'] < 18 :
            print("Sorry there isn't enough water.")
        elif drink_milk < reduced_resources['milk']:
            print("Sorry there isn't enough milk.")
        else:
            print("Sorry there isn't enough coffee")
        insufficient_ingredients = False
    elif enough_ingredients == 0:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        money_given = round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01), 3)

        money_return = round((money_given - drink_cost), 3)

        if money_return >= 0:
            reduced_resources = resource_reducer(drink_name, reduced_resources, drink_water, drink_milk, drink_coffee)
            print(f"Here is ${money_return} in change.")

            print(f"Here is your {drink_name}. Enjoy!!!")
        else:
            print("Sorry that's not enough money. Money refunded.")
        insufficient_ingredients = False
    else:
        insufficient_ingredients = False


