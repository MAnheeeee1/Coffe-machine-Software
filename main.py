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
def CalculatePrice_and_ReturnChange (order):
    cost = MENU[order]["cost"]
    #Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    amount_quarters = int(input("Insert your quarters: "))
    amount_dimes = int(input("Insert your dimes: "))
    amount_nickes = int(input("Insert your nickles: "))
    amount_pennies = int(input("Insert you pennies: "))
    amount_insertet = amount_quarters * 0.25 + amount_dimes * 0.25 + amount_nickes * 0.05 + amount_pennies * 0.01
    if amount_insertet < cost:
        print(f"Insufficient amount of money inserted!\nYou will get a refund of {amount_insertet}")
        return 2705
    else:
        return amount_insertet - cost
def sufficient_resources(order):
    required_milk = 0
    required_water = MENU[order]["ingredients"]["water"]
    if order != "espresso":
        required_milk = MENU[order]["ingredients"]["milk"]
    required_coffe = MENU[order]["ingredients"]["coffee"]
    if required_coffe <= resources["coffee"] and required_water <= resources["water"] and required_milk <= resources["milk"]:
        return True
    else:
        return False
def make_order(order):
    required_milk = 0
    required_water = MENU[order]["ingredients"]["water"]
    if order != "espresso":
        required_milk = MENU[order]["ingredients"]["milk"]
    required_coffe = MENU[order]["ingredients"]["coffee"]
    if required_coffe <= resources["coffee"] and required_water <= resources["water"] and required_milk <= resources["milk"]:
        resources["water"] -= required_water
        resources["milk"] -= required_milk
        resources["coffee"] -= required_coffe
        print(f"Here is your order :=), one {order}")
    else:
        print(f"Insufficient resources, please fill the machine!\nMachine stock:\n\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffe: {resources["coffee"]} ")
        print(f"Required resources to make one {order}: {MENU[order]["ingredients"]}")

machine_status = True
while machine_status == True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        machine_status = False
    elif order == "report":
        print(f"Machine resources\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffe: {resources["coffee"]}")
    elif order == "fill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Resources has been restocked!")
        print(f"Machine resources\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffe: {resources["coffee"]}")
    elif order == "espresso":
        if sufficient_resources(order) == True:
            change = round(CalculatePrice_and_ReturnChange(order), 2)
            if change > 0 and change != 2705:
                print(f"Here is {change}$ in change")
                make_order(order)
            #2705 its a error code that its returned if there its not enough money inserted
            elif change == 2705:
                print("You didn't insert enough money")
        else:
            print(f"Not enough resources to make a espresso\nCurrent stock:\n{resources}\nRequired: {MENU[order]["ingredients"]}")
    elif order == "latte":
        if sufficient_resources(order) == True:
            change = round(CalculatePrice_and_ReturnChange(order), 2)
            if change > 0 and change != 2705:
                print(f"Here is {change}$ in change")
                make_order(order)
            #2705 its a error code that its returned if there its not enough money inserted
            elif change == 2705:
                print("You didn't insert enough money")
        else:
            print(f"Not enough resources to make a espresso\nCurrent stock:\n{resources}\nRequired: {MENU[order]["ingredients"]}")
    elif order == "cappuccino":
        if sufficient_resources(order) == True:
            change = round(CalculatePrice_and_ReturnChange(order), 2)
            if change > 0 and change != 2705:
                print(f"Here is {change}$ in change")
                make_order(order)
            #2705 its a error code that its returned if there its not enough money inserted
            elif change == 2705:
                print("You didn't insert enough money")
        else:
            print(f"Not enough resources to make a espresso\nCurrent stock:\n{resources}\nRequired: {MENU[order]["ingredients"]}")
    else:
        print("Please chose a valid option (espresso/latte/cappuccino):")
