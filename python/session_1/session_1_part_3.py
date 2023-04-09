# try and except

try:
    print(x)
except:
    print('An exception occured')

# print(x)
print('string')


try:
    print(x)
except NameError:
    print('Variable is not defined')
else:
    print('Something went wrong')