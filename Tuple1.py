my_tuple = ('a', 'e', 'i', 'o', 'u', 'a', 'e', 'i')
#print(len(my_tuple))
#print(my_tuple.count('a'))
#print(my_tuple.index('o'))
my_list = list(my_tuple)
print(type(my_list))

my_tuple1 = tuple(my_list)
print(type(my_tuple1))

#slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[:5]
print(b)
b = a[::-1]     #reverse the tuple/list trick
print(b)

