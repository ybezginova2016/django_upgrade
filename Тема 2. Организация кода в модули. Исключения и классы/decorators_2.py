def decorator(class_link):
    print(f'I wrap the class {class_link}')
    return class_link

@decorator
class Cool:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'Cool, {self.string}'

cool = Cool('Python')
print(cool)

class OkButNotCool:
    def __str__(self):
        return 'Ok, but not cool :)'

def check(word):
    def decorator(class_link):
        if word != 'Python':
            return OkButNotCool
        return class_link
    return decorator

@check('C')
class Cool:
    def __str__(self):
        return f'Cool Python'

cool = Cool()
print(cool)
# результат выполнения программы:
# ok but not cool