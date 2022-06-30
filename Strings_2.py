my_string = '    hellow world    '
print(my_string)

my_string = my_string.strip()
print(my_string.upper())
print(my_string.startswith('h'))
print(my_string.endswith('h'))
print(my_string.find('w'))
print(my_string.count('w'))
print(my_string.replace('world', 'universe'))   #doesn't change the original string

print(my_string)

