class Vehicle:
    speed = 0
    age = 0

    def move(self):
        return f'Moving with speed{self.speed}'
class Car(Vehicle):
    # pass
    # speed = 130

    def __init__(self):
        self.speed = 130

car = Car()
v = Vehicle()

print(car.speed)
print(v.speed)

print()

print(car.move)
print(v.move)

print(Car, Car.__bases__, car, car.__class__)

'''
Car.__bases__ is a built-in attribute in Python that returns 
a tuple containing the base classes of the Car class. 
In other words, it returns the superclass of Car, which is 
Vehicle.

In the example you provided, Car is a subclass of Vehicle, 
meaning it inherits all the attributes and methods of Vehicle.
Since Car does not have any attributes or methods of its own, 
you used the pass statement to indicate that it is an empty 
class.
'''