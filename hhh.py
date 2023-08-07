ages = [10, 15, 25, 30, 19, 35, 14, 7, 11]
teenagers = []
adults = []
juniors = []

for age in ages:
    if age >= 21:
        adults.append(age)
    elif age <= 10:
        juniors.append(age)
    else :
        teenagers.append(age)

print(teenagers)
print(adults)
print(juniors)