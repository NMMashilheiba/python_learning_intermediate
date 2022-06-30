from itertools import groupby

#def smaller_then_3(x):
#    return x < 4
persons = [{'name': 'Timi', 'age': 25}, {'name': 'Dan', 'age':25}, {'name': 'Lisa', 'age': 27}, {'name': 'Jenny', 'age': 28}]

a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=lambda x: x < 4)                 #lambda function
for key, value in group_obj:
    print(key, list(value))

group_obj_1 = groupby(persons, key=lambda x: x['age'])      #lambda function
for key, value in group_obj_1:
    print(key, list(value))

