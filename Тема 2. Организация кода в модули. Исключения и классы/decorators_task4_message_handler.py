"""
был реализован чат-ботик, который распознает лишь одну команду start. Суть в том,
что на команду пользователя start он отвечает строкой okay, let's party!,
а на что-то другое строкой unrecognized command, do you mean "start"?

Напишите программку, в которой определите функцию start,
задекорированную функцией-декоратором message_handler на вывод
вышеописанного алгоритма чат-ботика.

входные данные: строка
результат: строка - реакция чат-ботика на команду пользователя
"""
def message_handler(func):
    def wrapper(command):
        if command.lower() == 'start':
            return func()
        else:
            return 'unrecognized command, do you mean "start"?'
    return wrapper

@message_handler
def start():
    return "okay, let's party!"

command = input()
print(start(command))
