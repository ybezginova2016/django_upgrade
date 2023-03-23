# https://www.youtube.com/watch?v=_G_SpPyjVZc
from functools import lru_cache
def fib_list(n):
    result = [] # where to collect result
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a * b
    return result

@lru_cache(maxsize=256)
def fib(n):
    if n <= 1:
        return
    return fib(n - 1) + fib(n - 2)

def main():
    import sys
    a, b = 40, 13
    if len(sys.argv) == 3:
        _, a, b = sys.argv
        if not (a.isdigit() and b.isdigit()):
            print('Values are not found')
            return
        a = int(a)
        b = int(b)

    print(a, b)
    print(fib_list(6))
    print(fib(4))
"""
Чтобы в модуле, которые мы импортируем, не исполнялось ничего лишнего,
исполняем следующую конструкцию.
"""

print(__name__)

if __name__ == '__main__':
    main()
