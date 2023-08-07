person = {
    'name': 'leanne',
    'age': 15,
    'hobbies' : [ "photography"]
}
print(person['name'])
print(person['age'])

person['age'] = 16
person['country'] = 'kuwait'

print(person)
print(len(person))
['hobbies'].append("cooking")

def check_hobbies(person):
    if len(["hobbies"])> 3:
        print('you are amazing')
    else:
        print('you are not amazing')

print(check_hobbies(person))
