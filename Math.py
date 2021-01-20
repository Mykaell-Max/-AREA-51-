# factorial
def factorial(n):
    f = 1
    for e in range(1, n+1):
        f *= e
    return f


# root
def root(n, r):
    return n ** 1/r
