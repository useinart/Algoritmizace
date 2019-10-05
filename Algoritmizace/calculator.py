import math

def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError('This operation is not supported for given input parameters')


def modulo(x, y):
    if x >= y and x > 0 and y > 0:
        return x % y
    else:
        raise ValueError('This operation is not supported for given input parameters')


def secondPower(x):
    return x**2


def power(x, y):
    if y >= 0:
        return float(x**y)
    else:
        raise ValueError('This operation is not supported for given input parameters')


def secondRadix(x):
    if x > 0:
        return math.sqrt(x)
    else:
        raise ValueError('This operation is not supported for given input parameters')


def magic(x, y, z, k):
    l = x + k
    m = y + z
    if m != 0:
        return (l/m) + 1
    else:
        raise ValueError('This operation is not supported for given input parameters')


def control(a, x, y, z, k):
    if a == 'ADDITION' or a == 1:
        return addition(x, y)
    elif a == 'SUBTRACTION' or a == 2:
        return subtraction(x, y)
    elif a == 'MULTIPLICATION' or a == 3:
        return  multiplication(x, y)
    elif a == 'DIVISION' or a == 4:
        return division(x, y)
    elif a == 'MOD' or a == 5:
        return modulo(x, y)
    elif a == 'POWER' or a == 7:
        return power(x, y)
    elif a == 'SECONDRADIX' or a == 8:
        return secondRadix(x)
    elif a == 'MAGIC' or a == 9:
        return magic(x, y, z, k)
    else:
        raise ValueError('This operation is not supported for given input parameters')



