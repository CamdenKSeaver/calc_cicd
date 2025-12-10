import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b
def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def log(x, base=math.e):
    if x <= 0:
        raise ValueError(" Must be > 0")
    if base <= 0 or base == 1:
        raise ValueError("Invalid log base")
    return math.log(x, base)

def square(x):
    return x ** 2

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def sqrt(x):
    if x < 0:
        raise ValueError("Cant use negative number")
    return math.sqrt(x)
