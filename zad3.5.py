import math
def monotoniczna(a1,a2):
    if (a1==a2):
        print("rownolegle")
    elif (a1 * a2==-1):
        print("prostopadla")
    else:
        print("ani rownolegla ani prostopadla")
a1 = int(input("podaj a"))
b1 = int(input("podaj b"))
c1 = int(input("podaj c"))
a2 = int(input("podaj a"))
b2 = int(input("podaj b"))
c2 = int(input("podaj c"))
print(monotoniczna(a1,a2))