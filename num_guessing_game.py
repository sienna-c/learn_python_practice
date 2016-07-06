import random as r
min = 1
max = 50
key = r.randint(min, max)

def numGuess():
    cal = 6
    print "Take a guess from %s to %s! You have 6 chances." % (min, max)
    while cal > 0:
        num = raw_input("Input a number: ")
        num = int(num)
        cal = cal - 1
        print "Counting down...%s" % cal

        if num < key:
            print "Too low"

        if num > key:
            print "Too high"

        if num == key:
            break

    if num == key:
        print "You got it!"
    else:
        print "You've lost"
