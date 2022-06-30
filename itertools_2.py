from itertools import accumulate
import operator
a = [1, 2, 3, 4]
a_1 = [1, 2, 3, 6, 8, 11, 4]
acc = accumulate(a)             #sum
acc_1 = accumulate(a, func=operator.mul)
acc_2 = accumulate(a_1, func=max)  
print(a)
print(list(acc))
print(list(acc_1))
print(list(acc_2))