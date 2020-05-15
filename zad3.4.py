import sys
import math
def monotoniczna(a):
    if (a>0):
        print ("rosnąca")
    elif (a==0):
        print("stała")
    else:
        print("malejąca")
a = int(input("podaj a"))
b = int(input("podaj b"))
c = int(input("podaj c"))
print(monotoniczna(a))