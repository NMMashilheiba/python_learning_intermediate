def outer_function(msg):
    #message = msg
    def inner_function():
        print(msg)
    #return inner_function()
    return inner_function

#outer_function('Hi')
my_func = outer_function('Hello from the waiting to be exe inner function')
my_func_1 = outer_function('hello ...')

my_func()
my_func_1()