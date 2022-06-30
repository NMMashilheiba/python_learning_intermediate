# variable length arguments (*args, **kwargs)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg, end=' ')
    print()
    for key in kwargs:
        print(key, '=', kwargs[key])
foo(1, 3, 9, 8, 7, 'eye', 'nose',  four=4, five=5)
