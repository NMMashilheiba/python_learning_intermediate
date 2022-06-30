# collections: counter, namedtuple, OrderedDict, defaultDict, deque 
from collections import Counter
a ="aaabbbbccc"
my_counter = Counter(a)
#print(my_counter.items())
#print(my_counter.values())
#print(my_counter.keys())
#print(my_counter.most_common(3))
#print(my_counter.most_common(3)[0])
#print(my_counter.most_common(3)[0][0])
print(list(my_counter.elements()))
