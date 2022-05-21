



def printOrder(order_number, order, quantity, type, addons, sugar,maddons, toast, mquantity, mtype):

    TAX_RATE = 0.0625
    
    muffin_price=3.00*mquantity

    if order == '1':
        total_price = 2.50 * quantity
    elif order == '2':
        total_price = 1.75 * quantity    
    else:
        total_price = 1.00 * quantity
        
    sales_tax = (total_price + muffin_price) * TAX_RATE
    net_price = total_price + sales_tax + muffin_price
    print('Receipt')
    print("Order #: {}".format(order_number))
    if order == '1':print('You have ordered {}'.format(quantity), 'Quaranta')
    if order == '2':print('You have ordered {}'.format(quantity), 'Grosso')
    if order == '3':print('You have ordered {}'.format(quantity), 'Lanky')
    if order == '4':print('You have ordered {}'.format(mquantity), 'Muffin')
    print('Coffee type: {}'.format(type))
    print('Addons: {}'.format(addons))
    print('Sugar: {}'.format(sugar))

    print('Muffin type: {}'.format(mtype))
    print('Addons: {}'.format(maddons))
    print('Toast: {}'.format(toast))

    my_float = total_price
    limit_float_total = round(my_float, 2)
    print('Gross total: $. {}'.format(limit_float_total))

    my_float = sales_tax
    limit_float_tax = round(my_float, 2)
    print('Sales tax: $. {}'.format(limit_float_tax))

    my_float = net_price
    limit_float_net = round(my_float, 2)
    print('Net total: $. {}'.format(limit_float_net))
    print('\n')
    

def main():

    
    orderAgain = 'y'
    order_number = 0
    while orderAgain == 'y' or orderAgain == 'yes':
        order_number += 1
        while True:
            print('Welcome to Monroe Coffee House')
            print('------------------------------\n')
            print('1. Quaranta @ $ 2.50')
            print('2. Grosso @ $ 1.75')
            print('3. Lanky @ $ 1.00')
            order = input('Enter your choice 1,2 or 3: ')
            if order == '1' or order == '2' or order == '3':
                break
            else:
                print('Sorry! Invalid selection.')
        quantity = int(input('How many orders you like to place? '))
        ctype = int(input('Enter coffee type - (1)Regular or (2)Decaf? '))
        if ctype == 1:
            type = "Regular"
        elif ctype == 2:
            type = "Decaf"
        else:
            pass

        caddons = int(input('Enter addons - (1)Black, (2)Milk or (3)Half/Half? '))
        if caddons == 1:
            addons = "Black"
        elif caddons == 2:
            addons = "Milk"
        elif caddons == 3:
            addons = "Half/Half"
        else:
            pass
        csugar = input('Do you need sugar? yes or no? ')
        if csugar == 'yes' or csugar== 'y':
            sugar = "Yes"
        elif csugar == 'no' or csugar == 'n':
            sugar = "No"
        else:
            pass
            
        mquantity = int(input('How many muffin orders you like to place? '))
        muffintype = int(input('Enter Muffin type - (1)Corn Muffin, (2)Blueberry muffin or (3)Chocolate chip muffin?'))
        if muffintype == 1:
            mtype = "Corn Muffin"
        elif muffintype == 2:
            mtype = "Blueberry muffin"
        elif muffintype == 3:
            mtype = "Chocolate chip muffin"
        else:
            print("invalid input")

        muffinaddons = int(input('Enter addons - (1)Blueberry, (2)Margarine or  (3)Orange Marmalade? '))
        if muffinaddons == 1:
            maddons = "Blueberry"
        elif muffinaddons == 2:
            maddons = "Margarine"
        elif muffinaddons == 3:
            maddons = "Orange Marmalade"
        else:
            pass

        mtoast = input('Do you need toasted muffin? yes or no? ')
        if mtoast == 'yes' or csugar== 'y':
            toast = "Yes"
        elif mtoast == 'no' or csugar == 'n':
            toast = "No"
        else:
            pass
        print('\nThanks for placing your order!')
        printOrder(order_number, order, quantity, type, addons, sugar, maddons, toast, mquantity, mtype )
        orderAgain = input('Do you want to order again? yes or no: ')
if __name__ == '__main__':
    main()





