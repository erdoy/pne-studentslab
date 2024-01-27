# --- Find the error!


def g(a, b):
    return a - b


def f(a, b, c, d):
    if c != d:
        t1 = g(c, d)
        t3 = 2 * (b / t1)
        return b + 2*t1 + t3*t3


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))
