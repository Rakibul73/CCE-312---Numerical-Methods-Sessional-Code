import numpy as np


def simpsonError(d4f, a, b, n):
    M = abs(d4f(b))
    if abs(d4f(a)) > abs(d4f(b)):
        M = abs(d4f(a))

    return (b - a) ** 5 * M / (180 * n ** 4)


def simpson(f, a, b, n):
    I = f(a) + f(b)
    h = (b - a) / n

    firstSum = 0
    for i in range(1, n // 2 + 1):
        xi = a + (2 * i - 1) * h
        firstSum += f(xi)

    secondSum = 0
    for i in range(1, n // 2):
        xi = a + 2 * i * h
        secondSum += f(xi)

    I += 4 * firstSum + 2 * secondSum
    I *= h / 3

    return I


if __name__ == "__main__":
    f = lambda x: 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

    print('%f' % (simpson(f, 0.2, 0.8, 2)), '%f' % simpsonError(f, 0.2, 0.8, 2))