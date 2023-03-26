class Ok:
    def __str__(self):
        return 'ok'

ok = Ok()

def wraper(class_link):
        print('ok', ok, sep=',', end=',')
        return class_link

@wraper
class Fine(Ok):
    def __str__(self):
        return super().__str__() + 'ey ' + 'fine!'

fine = Fine()
print(fine, end='')