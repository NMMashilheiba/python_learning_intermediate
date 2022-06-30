def foo(*args, last):           #here after *args, are keywords arguments
    for arg in args:
        print(arg, end=' ')
    print()
    print(last)

foo(1, 2, 3, last = 100)

def foo(a, b, *, c, d):         #here after *, are keywords arguments
    print(a, b, c, d)

foo(1, 2, c=22, d=33)