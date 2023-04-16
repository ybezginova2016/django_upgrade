from modtest import *
import modtest

print(f(3))
# print(_b(3)) # hidden name

print(modtest._b)

from modtest import _g
print(_g(5))