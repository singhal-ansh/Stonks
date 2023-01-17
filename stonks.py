# Welcome to Stonks! :D

# Defining some empty dicts that will come into play later
stocks = {}
more_than_0 = {}
history = {}


# Defining some functions to perform certain tasks

# Function to add stonks
def add_stonks(x, y):
    # This function will check if the inputted item is already present in the dictionary keys. If the item is not present, then the function will assign the inputted quantity as the item's value. However, If the item is already present, it will add the quantity to the pre-existing value.

    if x in stocks.keys():  # If item present
        stocks[x] = stocks[x] + y

    else:
        stocks[x] = y

    print('Your stocks have been updated: ')
    print(stocks)


def buy_stonks(x, y):
    # This function will check if the inputted item is already present in the dictionary keys. If it isn't then it will let the user know that the stock they want to purchase isn't available.
    if x in stocks.keys():

        if stocks[x] >= y:

            stocks[x] = stocks[x] - y
            print(f'''
Congratulations! You have successfully purchased {y} shares of {x}!''')
            print('')
            print('The updated stocks are:')
            print(stocks)
            history[f'"item_requested" = {x}, "amount requested" = {y}'] = '"status" = successful'

        else:
            print('Insufficient quantity!')
            history[f'"item_requested" = {x}, "amount requested" = {y}'] = '"status" = unsuccessful'

    else:
        print('No stocks available :(')
        history[f'"item_requested" = {x}, "amount requested" = {y}'] = '"status" = unsuccessful'


def show():
    for x in stocks.keys():
        if stocks[x] > 0:
            more_than_0[x] = stocks[x]


while 1:
    print(''' 
Welcome to Stonks! :D

Enter "add" to add stocks for an item,
Enter "purchase" to purchase stocks for an item,
Enter "display" to display current stocks (greater than zero),
Enter "history" to print all purchase orders.
Enter "stop" to exit Stonks   :( 

''')

    op = input('What do you want to do? ')

    if op == "add":
        print('')
        item = input('Enter item name: ')
        quant = int(input('Enter item quantity: '))
        add_stonks(item, quant)
        print('')

    elif op == "purchase":
        print('')
        buy = input('''
Which stock would you like to purchase? ''')
        amount = int(input(f'''
How many shares of {buy} would you like to purchase? '''))
        buy_stonks(buy, amount)
        print('')

    elif op == "display":
        print('')
        show()
        print(more_than_0)
        print('')

    elif op == "history":
        print('')
        print(history)
        print('')

    elif op == "stop":
        break
