# List comprihension
list_original = mylist = ["banana", "apple", "kiwi"]
#list_copy = list_original
list_copy = list_original.copy()
print(list_copy)

list_copy = list(list_original)
print(list_copy)


list_copy = list_original[:]
print(list_copy)

#List comprehension     -> syntax: var = [expression for item in iterable if condition == True]
list_num = [1, 3, 5, 6]
new = [i*i for i in list_num]
print(new)

