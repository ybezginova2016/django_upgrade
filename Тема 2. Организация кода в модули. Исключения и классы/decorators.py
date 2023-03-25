# декораторы в Python - это конструкция, которая позволяет изменить
# поведение, например, функций или классов, т.е. выполнить определенные
# действия перед их выполнением
"""
def decorator(link):  # функция-декоратор
    return link       # возвращение ссылки на декорируемый объект


@decorator            # вызов функции-декоратора на декорируемый объект
object
"""

def decorator(function):
    print(f'I wrap the function {function}')
    return function

@decorator
def cool(string):
    return f'cool {string}'

print(cool('python'))
