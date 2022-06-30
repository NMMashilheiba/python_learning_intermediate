#unpack
my_tuple = "Max", 23, "NewYork"
my_tuple1 = 0, 1, 2, 3, 4, 5

name, age, city = my_tuple
print(name)
print(age)
print(city)

i1, *i2, i3 = my_tuple1
print(i1)
print(i2)
print(i3)
