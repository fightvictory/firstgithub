def sum(a, b):
    return a + b

# print(sum('Java', ' Python'))

X = 99
def func():
    global X
    X = 88
func()
print(X)

y, z = 1, 2
def all_global():
    global x
    x = y + z
all_global()
print(x)

def func1(Y):
    Z = X + Y
    return Z
print(func1(1))

def func2(a, b=5, c=100):
    return a + b + c
print(func2(10, c=20))

def func3(a, b, *name):
    return name

print(func3('a', 'b'))

def func4(**name):
    return name
print(func4(a=1, b=2))

def func5(a, b, *arg, **name):
    print(a, b)
    print(arg)
    print(name)
func5(1, 2, 3, 4, 5, 6, x=1, y=2, z=3)

f = lambda x, y, z: x + y + z
print(f(3, 4, 5))
