# local vs. global functions

def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)
    print(number+1)

number = 0                  # global variable
foo()
print(number)
