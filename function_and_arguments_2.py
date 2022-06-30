# container unpacking into function arguments using asterisk operator
def foo(a, b, c):
    print(a, b, c)

my_list = [2, 4, 6]
my_tuple = (3, 5, 7)
my_dict = {'a': 11, 'b': 12, 'c': 13}

foo(*my_list)
foo(*my_tuple)
foo(**my_dict)
