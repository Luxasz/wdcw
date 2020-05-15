import sys
import numpy
mac=numpy.random.randint(1,10, size=(4,4))
a = [mac[index_x][index_x] for index_x, x in enumerate(mac)]
print(mac)
print(a)
