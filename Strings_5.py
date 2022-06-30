#fromatting: %, .format(), f-strings

var = 'Tom'
var_1 = 3
var_2 = 3.14159265358979

string = "the variable is %.10f" %var_2
print(string)

string_1 = "the variable is {:.5f} and {}".format(var_2, var)
print(string_1)

string_2 = f"the variable is {var_1 * var_1}, {var} and {var_2}"
print(string_2)

