# Shallow copy
import copy
original = [1, 2, 3]
#copy = copy.copy(original)
copy = original.copy()
#copy = list(original)
#copy = original[:]
copy[1] = 9
print(copy)
print(original)