menu = [ 'coffee' , 'water' , 'juice' , 'cookie', 'cake' ]
coffee = 3
water = 1
juice = 2
cookie = 4
cake= 6
budget = int(input('whats your budget?'))
if budget >= 6:
    print('you can buy:')
    for thing in menu:
        print(thing)
elif budget >= 4:
    menu.remove('cake')
    print('you can buy:')
    for thing in menu:
        print(thing)
    menu.insert(4,'cake')
elif budget >= 3:
    menu.remove('cake')
    menu.remove('cookie')
    print('you can buy:')
    for thing in menu:
        print(thing)
    menu.insert(4,'cake')
    menu.insert(3,'cookie')
elif budget >= 2:
    menu.remove('cake')
    menu.remove('cookie')
    menu.remove('coffee')
    print('you can buy:')
    for thing in menu:
        print(thing)
    menu.insert(4,'cake')
    menu.insert(3,'cookie')
    menu.insert(0, 'coffee')
elif budget >= 1:
    menu.remove('cake')
    menu.remove('cookie')
    menu.remove('coffee')
    menu.remove('juice')
    print('you can buy:')
    for thing in menu:
        print(thing)
    menu.insert(4,'cake')
    menu.insert(3,'cookie')
    menu.insert(0, 'coffee')
    menu.insert(2, 'juice')
else : 
    print('you can only buy water')
