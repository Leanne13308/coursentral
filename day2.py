my_name = input('whats your name?')
my_age = input('whats your age?')
print(f'my name is {my_name} , i am {my_age} years old')


first_number = int(input('enter your first number'))
second_number = int(input('enter your second number'))
operation = input('enter an operation')
if operation == "+":
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/':
    print(first_number / second_number)
else:
    print('the operation is not valid')


bus_capacity = 15
used_seats = int(input('how many people are in the bus?'))
new_passangers = int(input('how many people want to board the bus?'))
empty_seats = bus_capacity - used_seats 
if empty_seats >= new_passangers:
    print(f'there are {empty_seats} empty seats')
else:
    print('sorry the bus is full')
