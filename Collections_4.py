from collections import deque
d = deque()

d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)

d.extend([4, 5, 6])
print(d)

d.rotate(-1)
print(d)
