a = 10
b = 0

def f():
    global b
    c = a*a
    b = c

f()
print(b,a)

