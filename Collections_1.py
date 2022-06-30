from collections import namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, 3)
print(pt)
print(pt.x, pt.y)