odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

setA = {1, 2,3, 4, 5 , 6, 7, 8, 9}
setB = {1, 2, 3, 10, 12, 14}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

difference = setB.difference(setA)
print(difference)

symmetric_diff = setA.symmetric_difference(setB)
print(symmetric_diff) 

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.difference_update(setB)
print(setA)

#all set operation are are valid...