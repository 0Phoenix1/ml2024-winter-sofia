# TODO: 1. list of requirements for making coffee(coffee, sugar, water, milk)
menu={
    'espresso':{
        'ingredients':{
            'water':50,
            'coffee': 18
        },
        'cost':1.5
    },
    'latte':{
        'ingredients': {
            'water':200,
            'milk':150,
            'coffee': 24

        },
        'cost':2.5
    },
    'cappuccino':{
        'ingredients':{
            'water': 250,
            'milk':100,
            'coffee':24

        },
        'cost':3
    }
}
resources ={
    'water':300,
    'milk':200,
    'coffee':100
}

def check_resources(drink):
    for item in drink:
        if drink[item]>resources[item]:
            print(f'Not enough {item}')
            return False
    return True

def coin():
    """Total Money in Dollars"""
    print('Please insert coins:')
    total=int(input('How many pennies: '))*.01
    total+=int(input('How many nickles: '))*.05
    total+=int(input('How many dimes: '))*.1
    total+=int(input('How many quarter: '))*.25

    return total


def deduct_ingredients(drink_name, order_ingredient):
    """Deduct the ingredients used from the resources
    :type resources: ingredient
    """
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f'Here is your {drink_name} ')
        



def is_transaction_successful(payment,price):
    """Return True if payment is successful,
    else return False"""
    if payment>=price:
        change=round((payment-price),2)
        if change>0:
            print(f'Here is your change: ${change}')

        global profit
        profit+=price
        return True
    else:
        print('Sorry the payment is not enough')
        return False





profit=0
is_on=True
while is_on:
    choose=input('What coffee do you want (latte/espresso/cappuccino): ').lower()
    if choose=='off':
        is_on=False
    elif choose=='report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f'Coffee:{resources["coffee"]} gm')
        print(f'Money: ${profit} ')

    else:
        drink=menu[choose]

        if check_resources(drink['ingredients']):
            payment = coin()
            if is_transaction_successful(payment,drink['cost']):
                deduct_ingredients(choose,drink['ingredients'])








