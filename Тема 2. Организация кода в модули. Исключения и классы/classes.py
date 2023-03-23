class MyClass(object):
    pass

print(MyClass, type(MyClass), MyClass.__bases__)

class Human:
    pass

h = Human()
h.name = 'John'
h.age = 42

def print_human(human):
    print(Human)
    print(human.name, human.age)

print_human(h)

class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()
print(p.x, p.y)

class Point2(object):
    attr = 32

    # инициализатор, в котором происходит инициализация
    # объекта класса
    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point2(13, 3)
print(p2.x, p2.y)
print(p2.attr)

p2.attr = 40

p3 = Point2(0, 0)
p3.attr = 50

print(p2.attr, p3.attr, Point.attr)

print(p.attr)

print()

# проверяем, принадлежит ли объекту класса
print(isinstance(h, Human))
print(isinstance(p, Point))
print(isinstance(p2, Point2))

print(isinstance(h, (Human, Point)))

l = []
print(isinstance(l, Point2))
