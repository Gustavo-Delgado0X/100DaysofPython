def report(resource):
    """Generate Report of all Resources"""
    # TODO: 1 Print the report of all the coffee machine resources

    for key in resource:
        if key == 'water':
            print(f"{key}: {resource[key]}ml")
        elif key == 'milk':
            print(f"{key}: {resource[key]}ml")
        elif key == 'coffee':
            print(f"{key}: {resource[key]}g")
    print(f"money: ${money}")

def sufficient_resource(ingredient):
    """Checks if there are sufficient resources for the drink"""
    for item in ingredient:
        if  ingredient[item] > resources[item]:
            print(f"sorry not enough ingredients: {item}")
            return False
    return True

def process_coins():
    """Processes the payment"""
    # TODO: 3 Process Coins
    print("Insert Coins")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    total_payed = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total_payed

def transaction(coins_inserted,cost_drink):
    """Process payment and Refund"""
    # TODO: 4 Check Transaction Successful
    global money

    if coins_inserted >= cost_drink:
        money += cost_drink
        refund = coins_inserted - cost_drink
        print(f"transaction complete, Refund: ${refund:.2f}")
    elif coins_inserted < cost_drink:
        print("Sorry That's not enough Money. Money Refunded")
        return False
    return True

def make_coffee(ingredient,drink_name):
    """Delivers the coffee"""
    # TODO: 5 Make Coffee

    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {drink_name}☕")
    
MENU = {
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

money = 0

machine_on = True

while machine_on:

    # TODO: 2 Check resources sufficient to make drink order
    selection = input("Choose a drink 'espresso','latte', or 'cappuccino': ")
    
    if selection == "report":
        report(resources)
    elif selection == "off":
        machine_on = False
        print("Turning Off")
    else:
        drink_ingredient = MENU[selection]["ingredients"]
        if sufficient_resource(drink_ingredient):

            drink_cost = MENU[selection]["cost"]
            inserted_coins = process_coins() 
            if transaction(coins_inserted=inserted_coins,cost_drink=drink_cost):
                
                make_coffee(ingredient=drink_ingredient,drink_name=selection)
        


# #Angela's Solution

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
