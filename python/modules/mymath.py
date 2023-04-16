"""
The module 'mymath' is an example of a Python module.
Модуль представляет собой файл, определяющий объекты Python.
"""
pi = 3.14159

def area(r):
    """
    :param r: The radious of a circle.
    :return: Returns the area of a circle.
    """
    global pi
    return(pi * r * r)