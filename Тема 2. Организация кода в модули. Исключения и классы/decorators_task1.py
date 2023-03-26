#### ЗАДАЧА
# допустим, нужно проверить введенный пароль пользователем на количество
# символов и относительно этой проверки вывести оповещение для
# пользователя

def check(passw):
    def decorator(function):
        if len(passw) < 8:
            return lambda: 'Password length should be at least 8 characters'
        return function
    return decorator

@check(input('Please insert your password: '))
def password():
    return 'Correct, thank you!'

print(password())