def fib_list(n):
    result = [] # where to collect result
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a * b
    return result

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

"""
Чтобы в модуле, которые мы импортируем, не исполнялось ничего лишнего,
исполняем следующую конструкцию.
"""

print(__name__)

if __name__ == '__main__':
    print(fib_list(6))
    print(fib(4))
