import sys
import math
import random
def funkcja(a,b,x,y):
    return math.sqrt(((x-a)**2)+((y-b)**2))
a=random.randint(1,10)
b=random.randint(1,10)
x=random.randint(1,10)
y=random.randint(1,10)
print(funkcja(a,b,x,y))