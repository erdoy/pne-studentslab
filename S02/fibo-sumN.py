def fibosum(n):
    v1 = 0
    v2 = 1
    sum = 0

    for i in range(n):
        v2 = v2 + v1
        v1 = v2 - v1
        sum += v1

    return sum


print("The sum of the first 5 elements of the fibonacci sequence:", fibosum(5))
print("The sum of the first 10 elements of the fibonacci sequence:", fibosum(10))
