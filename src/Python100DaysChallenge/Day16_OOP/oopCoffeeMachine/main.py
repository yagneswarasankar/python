from src.Python100DaysChallenge.Day16_OOP.oopCoffeeMachine.menu import  Menu, MenuItem
from src.Python100DaysChallenge.Day16_OOP.oopCoffeeMachine.coffee_maker import CoffeeMaker
from src.Python100DaysChallenge.Day16_OOP.oopCoffeeMachine.money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on:
    option = menu.get_items()
    choice = input(f"What drint you want ({option}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


