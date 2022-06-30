from itertools import count, cycle, repeat 
from timeit import default_timer as timer

start = timer()
for i in count(10):
    print(i)
    if i == 100:
        break
stop = timer()
print(stop - start, "sec")

#a = [1, 2, 3]
#for i in cycle(a):
#    print(i)

a = [1, 2, 3]
for i in repeat(a, 2):
    print(i)
