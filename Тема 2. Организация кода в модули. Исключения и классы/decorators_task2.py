digits = [1, -2, -5, 1, 4, 3, -3, 2]

def balance(a):
    def wrapper(f):
        if sum(a) != 0:
            return lambda: 'There is no balance :('
        return f
    return wrapper

@balance(digits)
def check():
    return 'Cool, it is balanced :)'

print(check(), end='')