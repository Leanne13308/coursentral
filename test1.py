budget = int(input('how much is your budget?'))
coffee = 3
cookie = 2
water = 1
if budget >= 2*coffee:
    print('you can buy two coffees')
elif budget >= coffee:
    print('you can buy one coffee')
else:
    print('you cant buy coffee')