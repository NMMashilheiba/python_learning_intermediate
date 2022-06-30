from typing import Sized
import sys

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
#print(sys.getsizeof(fib))
for i in fib:
    print(i, end=' ')

