#redeuce(func, seq)
from functools import reduce
mylist = [1, 2, 3, 4, 5]

product_a = reduce(lambda x, y: x*y, mylist)
print(product_a)

