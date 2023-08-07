def my_filtering_function(pair):
    key, value = pair
    if len(key) != 4:  # first condition
        return False
    if key[0] != 'M':
        return False  # second condition
    if value <= 8.9:
        return False  # third condition
    # If nothing was returned until here, it means that
    # the pair passed all conditions. Keep it in the dictionary!
    return True
 
grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}
 
filtered_grades = dict(filter(my_filtering_function, grades.items()))
 
print(filtered_grades)