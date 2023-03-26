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
# результат выполнения программы:
# I wrap the function <function cool at 0x0000020096071790>
# cool python

"""
конструкция @decorator указывает на функцию-декоратор decorator(function) 
для функции cool, т.е. функция decorator становится оберткой для функции 
cool, которая выполняется ~ раскрывается перед выполнением самой функции 
cool 
в параметр функции decorator поступает ссылка на функцию, которую она 
оборачивает, эту ссылку можно видеть в результате выполнения программы 
<function cool at 0x0000020096071790>
"""
print()

print(decorator(cool)('python'))