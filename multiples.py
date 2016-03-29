def printMultiples(n):
    i = 1
    while i <= 9:
        print n*i, "\t",  # Why do we need the comma?
        i = i+1
    print
i = 1
while i <= 9:
    printMultiples(i)
    i = i+1
