import copy
original = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
copy = copy.deepcopy(original)
copy[0][1] = -12
print(original, 'original')
print(copy, 'copy')