# immutable object can't be change
def foo(x):
    x = 5

var = 10                # immutable
foo(var)
print(var)      

def foo(a_list):
    a_list.append(4)
    a_list[0] = 9       # immutable inside a mutable can be change

my_list = [1, 2, 3]     # mutable    
foo(my_list)
print(my_list)

