# sorted(iterable, key=key, reverse=reverse)    
# -> sorted() sorts each elements based on the key
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]           
'''def sort_by_y(x):
    print(x[1])
    return x[1]'''

points2D_sorted = sorted(points2D)
points2D_sorted_1 = sorted(points2D, key = lambda x: x[1])
points2D_sorted_2 = sorted(points2D, key = lambda x: x[0] + x[1])

#print(points2D)
print(points2D_sorted)
print(points2D_sorted_1)
print(points2D_sorted_2)