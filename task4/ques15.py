

from functools import reduce

l = [1,2,7,8,9,6,7,8]
print(reduce(lambda x,y: x*y ,l))
