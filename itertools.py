# itertools: product, permutation, combination, accumulate, groupby, and infinite iterators
from itertools import product
a = [1, 2]
b = [4]
prod = product(a,b, repeat=2)
print(list(prod))

