
water = 400
milk = 540
beans = 120
cups = 9
money = 550
drink = ""
action = ""


def add_water():  # if not enough water
    print("Sorry, not enough water")


def add_milk():  # if not enough milk
    print("Sorry, not enough milk")


def add_beans():  # if not enough beans
    print("Sorry, not enough coffee beans")


def add_cups():  # if out of cups
    print("Sorry, not enough disposable cups")


def enough():  # if enough supplies
    print("I have enough resources, making you a coffee!")


def buy_ask():  # ask action in 'buy'
    global drink
    drink = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")  # read drink input
    return drink


def start():
    global action
    global water
    global milk
    global beans
    global cups
    global money
    global drink
    action = input("\nWrite action (buy, fill, take, remaining, exit): \n")
    if action == "buy":
        buy_ask()
        if cups < 1:  # check if not out of cups
            add_cups()
        if drink == "1":  # check supplies and make 1
            if water < 250:
                add_water()
            elif beans < 16:
                add_beans()
            else:
                enough()
                water -= 250
                beans -= 16
                money += 4
                cups -= 1
                return water, milk, beans, cups, money
        elif drink == "2":  # check supplies and make 2
            if water < 350:
                add_water()
            elif milk < 75:
                add_milk()
            elif beans < 20:
                add_beans()
            else:
                enough()
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                cups -= 1
                return water, milk, beans, cups, money
        elif drink == "3":  # check supplies and make 3
            if water < 200:
                add_water()
            elif milk < 100:
                add_milk()
            elif beans < 12:
                add_beans()
            else:
                enough()
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                cups -= 1
                return water, milk, beans, cups, money
        elif drink == "back":
            start()
    elif action == "fill":
        water_add = int(input("\nWrite how many ml of water do you want to add: \n"))
        milk_add = int(input("Write how many ml of milk do you want to add: \n"))
        beans_add = int(input("Write how many grams of coffee beans do you want to add: \n"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add: \n"))
        water += water_add
        milk += milk_add
        beans += beans_add
        cups += cups_add
    elif action == "take":
        print("I gave you $", money, sep='')
        money = 0
    elif action == "remaining":
        print("\nThe coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(beans, "of coffee beans")
        print(cups, "of disposable cups")
        print(money, "of money ")


while action != "exit":
    start()
