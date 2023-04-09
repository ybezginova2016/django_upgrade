u = (3,4)
v = (3,6)
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])
def subtract(a,b):
    return (a[0] - b[0], a[1] - b[1])
def dot(a, b):
    return (a[0] * b[0] + a[1] * b[1])
def norm(a):
    return (a[0] * a[0] + a[1] * a[1]) ** 0.5
def isvertical(a):
    return a[0] == 0

print(norm(u))
print(add(u,v))
print(u + v)
print(isvertical(subtract(v, u)))