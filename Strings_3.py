my_string = 'how are you doing?'
my_list = my_string.split()         #default delimiter is whitespace
print(my_list)

#convert string into list
my_string_1 = 'how,are,you,doing?'
my_list_1 = my_string_1.split(",")  #here delimiter is comma
#print(my_list_1)

#back to string
new_string = ' '.join(my_list)
print(new_string)

