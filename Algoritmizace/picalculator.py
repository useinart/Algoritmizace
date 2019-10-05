import math

def leibnizPi(iterations):
    pi = 0
    numerator = 4
    for num in range(iterations):
        denominator = 1 + (2 * num)
        fraction = numerator/denominator
        if num % 2 == 0:
            pi += fraction
        else:
            pi -= fraction
    return pi


def nilakanthaPi(iterations):
    pi = 0
    for num in range(iterations):
        if num == 0:
            numerator = 3
            pi += numerator
        else:
            numerator = 4
            denominator = (num * 2) * ((num * 2) + 1) * ((num * 2) + 2)
            fraction = numerator/denominator
            if num % 2 == 0:
                pi -= fraction
            else:
                pi += fraction
    return pi


def newtonPi(init):
    x = float(init)
    xnew = 0
    while xnew != x:
        xnew = float(x)
        x = x - (math.sin(x)/math.cos(x))
    return float(xnew)


print(newtonPi(-3.0))




