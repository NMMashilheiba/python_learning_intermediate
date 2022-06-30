# filter(func(), seq)     -> func() return true or false and 
# filter() return all the elements for which the function func() evaluate to true 
mylist = [1, 2, 3, 4, 5]

a = filter(lambda x: x%2==0, mylist)
print(list(a))

b = [i for i in mylist if i%2==0]
print(b)
