# map(func, seq)    -> transforms each elements with a function
mylist = [1, 2, 3, 4, 5]

# bad code i.e code is not clean
# print(list(map(lambda x: x*2, mylist)))

a = map(lambda x: x*2, mylist)
print(list(a))
# the same can be achieve using list comprehension
b = [for i in mylist]
print(list(b))

