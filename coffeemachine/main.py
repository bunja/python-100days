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


# user_answer = input("What would you like to drink: espresso/cappuccino/latte?")
# user_choice = MENU[user_answer]
# print(user_choice)

def check_resources(resources, user_choice):
    resources_needed = user_choice['ingredients']
    keys = resources.keys()
    for key in keys:
        if resources[key] < resources_needed.get(key, 0):
            return False
    return True

def update_resources(resources, user_choice):
    resources_used = user_choice['ingredients']
    keys = resources.keys()
    for key in keys:
        resources[key] = resources[key] - resources_used.get(key, 0)


def print_report(resources, money):
    print(f"Resources left {resources}")
    print(f"Money {money}")


def process_coins():
    quarters = int(input('how many quarters do you insert?'))
    dimes = int(input('how many dimes do you insert?'))
    nickles = int(input('how many nickles do you insert?'))
    pennies = int(input('how many pennies do you insert?'))

    user_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return user_money


# print(process_coins() )


def check_money(user_money, cost):
    if cost > user_money:
        return -1
    elif cost == user_money:
        return 0
    else:
        return user_money - cost


def make_coffee():
    money = 0
    is_off = False
    while not is_off:
        user_answer = input("What would you like to drink: espresso/cappuccino/latte?")
        if user_answer == "off":
            is_off = True
            return
        elif user_answer == "report":
            print_report(resources, money)
            continue
        user_choice = MENU[user_answer]
        choice_cost = user_choice['cost']

        if check_resources(resources, user_choice):
            print("Please, insert the money")
            user_money = process_coins()
            if check_money(user_money, choice_cost) == -1:
                print("not enough money")
                return
            else:
                change = check_money(user_money, choice_cost)
                print(f" thanks.. this is your change{change}")
                update_resources(resources, user_choice)
                money = money + choice_cost
                print(f"enjoy your {user_answer}")
        else:
            print("Not enough resources")


make_coffee()



