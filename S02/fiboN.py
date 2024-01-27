def fibon(n):
    v1 = 0
    v2 = 1

    for i in range(n):
        v2 = v2 + v1
        v1 = v2 - v1

    return v1


print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))
