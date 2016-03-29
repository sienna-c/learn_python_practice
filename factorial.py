def factorial(n):
    if not isinstance(n, int):
        print "Factorial is only defined for integers."
        return -1
    elif n < 0:
        print "Factorial is only defined for positive intergers."
        return -1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
