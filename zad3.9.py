import sys
import math
import random
def iloczyn1(a1,r,liczba):
    iloczyn=a1
    i=1
    for i in range(liczba):
        iloczyn*=a1+i
        i += 1
    return iloczyn
a1=int(1)
r=int(1)
liczba=int(10)
print(iloczyn1(a1,r,liczba))