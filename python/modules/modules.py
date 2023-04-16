import mymath, importlib
# https://docs.python.org/3/reference/import.html

print(mymath.pi)
print(mymath.area(2))

print(mymath.__doc__)
print(mymath.area.__doc__)

print(importlib.reload(mymath))

import sys
print(sys.path) # _список каталогов в пути поиска_


