from menu import Menu  # MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffee_menu = Menu()
    money_related = MoneyMachine()
    coffee_make = CoffeeMaker()
    coffee_making = True
    while coffee_making:
        items = coffee_menu.get_items()
        coffee_type = input(f"What would you like? ({items}):").lower()
        if coffee_type == "report":
            coffee_make.report()
            money_related.report()
        elif (coffee_type == "espresso") or (coffee_type == "latte") or (coffee_type == "cappuccino"):
            y = coffee_menu.find_drink(coffee_type)
            if y is not None:
                resource_status = coffee_make.is_resource_sufficient(y)
                if resource_status is True:
                    money_status = money_related.make_payment(y.cost)
                    # print(money_status)
                    if money_status is True:
                        coffee_make.make_coffee(y)
                    elif money_status is False:
                        continue
                else:
                    continue
        elif coffee_type == "end":
            coffee_making = False
        else:
            print("wrong input! Please enter again")


if __name__ == '__main__':
    coffee_machine()

