from timeit import default_timer as timer

my_list = ['a'] * 2500000
#print(my_list)

# bad code
start = timer()
my_string = ''
for i in my_list:
    my_string += i
#print(my_string)
stop = timer()
print(stop - start)

# good code
start1 = timer()
my_string_1 = ''.join(my_list)
#print(my_string_1)
stop1 = timer()
print(stop1 - start1)
