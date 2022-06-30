# merging list and tuple with asterisk operator 
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_list, *my_tuple, *my_set]
print(new_list, '\n')

# can also merge dictionary
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'c': 4, 'd': 5, 'e': 6}
my_dict = {**dict_a, **dict_b}
print(my_dict)

