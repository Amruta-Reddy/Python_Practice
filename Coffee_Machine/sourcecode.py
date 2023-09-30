from coffee_data import resources, MENU

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

shop_open = True

while shop_open:
    coffee_name = input("What would you like? (espresso/latte/cappuccino):  ")

    if coffee_name == 'report':
        print(f"Water : {water}ml \nMilk  : {milk}ml \nCoffee : {coffee}g \nMoney : ${money}")

    else:
        if coffee_name in MENU:
            print("Please insert coins.")
            quarters = int(input("How many quarters? : ")) * 0.25
            dimes = int(input("How many dimes? : ")) * 0.10
            nickles = int(input("How many nickles? : ")) * 0.05
            pennies = int(input("How many pennies? : ")) * 0.01
            money_inserted = quarters + dimes + nickles + pennies
            change = round(money_inserted - MENU[coffee_name]['cost'], 2)

            if coffee_name == 'espresso':
                if money_inserted < MENU[coffee_name]['cost']:
                    print("Sorry money is not sufficient.")

                elif water < MENU[coffee_name]['ingredients']['water'] or coffee < MENU[coffee_name]['ingredients']['coffee']:
                    print("Sorry there is not enough resources")
                    shop_open = False
                else:
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {coffee_name} ☕️. Enjoy!")
                    water -= MENU[coffee_name]['ingredients']['water']
                    if coffee_name == 'espresso':
                        milk = milk
                    else:
                        milk -= MENU[coffee_name]['ingredients']['milk']
                    coffee -= MENU[coffee_name]['ingredients']['coffee']
                    money += MENU[coffee_name]['cost']

            else:
                if money_inserted < MENU[coffee_name]['cost']:
                    print("Sorry money is not sufficient.")

                elif water < MENU[coffee_name]['ingredients']['water'] or milk < MENU[coffee_name]['ingredients']['milk'] or coffee < MENU[coffee_name]['ingredients']['coffee']:
                    print("Sorry there is not enough resources")
                    shop_open = False
                else:
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {coffee_name} ☕️. Enjoy!")
                    water -= MENU[coffee_name]['ingredients']['water']
                    if coffee_name == 'espresso':
                        milk = milk
                    else:
                        milk -= MENU[coffee_name]['ingredients']['milk']
                    coffee -= MENU[coffee_name]['ingredients']['coffee']
                    money += MENU[coffee_name]['cost']





