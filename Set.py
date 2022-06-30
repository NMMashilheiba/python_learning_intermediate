#Sets: unordered, mutable, NO Duplicates
my_set = {1, 2, 3, 3, 2, 1}
my_set_1 = set([1, 2, 3, 4, 1, 2, 3])
my_set_2 = set("hello")

#print(my_set_1)
#print(my_set_2)
my_set.add(11)
my_set.add(21)
my_set.add(31)
my_set.remove(3)
my_set.discard(4)    #same as remove but no error if element not found
#print(my_set.pop())
print(my_set)

#Creating an empty set
my_empty_set = {}        #wrong! this is dictionary
my_Empty_set = set()
#print(type(my_Empty_set))


