favorite_animals = ['dog', 'cat', 'monkey', 'rabbit']
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.pop(2)
print(favorite_animals)

favorite_animals.append('snake')
for animal in favorite_animals:
    print(f'i love {animal}')


numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
for num in numbers:
    numbers_sum += num

print(numbers_sum)