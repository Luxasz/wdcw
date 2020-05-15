import sys
import numpy
produkty={"pietruszka":"kg", "wino": "l"}
a=[name for name, value in produkty.items() if value =="l"]
print(a)
