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

def printReport():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')

def checkForResources(orderIngradients):
    for item in orderIngradients:
        if orderIngradients[item] > resources[item]:
            print(f"There is no sufficient {item}: ")
            return False
    else:
       return True

def processCoins(choice):
    global money
    print("Please insert coins.")
    quarters = int(input("how many quarters?($0.25): "))
    dimes = int(input("how many dimes?($0.10): "))
    nickles = int(input("how many nickles?($0.05): "))
    pennies = int(input("how many pennies?($0.01): "))
    amount = quarters * (0.25) + dimes * (0.10) + nickles * (0.05) + pennies * (0.01)
    return amount

def transcationSuccess(money_recieved,cost_of_drink):
    global money
    if money_recieved >= cost_of_drink:
        change = round(money_recieved - cost_of_drink,2)
        print(f"Here is ${change} in change.")
        money += cost_of_drink
        return True
    else:
        print("Sorry money not sufficient. Money is returned")
        return False


def makeCoffee(drinkName,order_ingradients):
    for item in order_ingradients:
        resources[item] -= order_ingradients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")

inputProvided = True
while inputProvided:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        printReport()
    elif choice == "off":
        print("The machine is in maintanance")
        inputProvided = False
    else:
        drink = MENU[choice]
        if checkForResources(drink["ingredients"]):
            payment = processCoins(choice)
            if transcationSuccess(payment, drink["cost"]):
                makeCoffee(choice,drink["ingredients"])



















