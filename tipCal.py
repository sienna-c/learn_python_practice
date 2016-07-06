import rates

def priceCal():
    cost = raw_input("How much is the meal you ordered: $")
    try:
        cost = float(cost)
        #tax = 6.75/100
        #tipRate = 15.0/100
        total = cost + cost * rates.tax
        tip = total * rates.tipRate
        addTips = total + tip
        print "tip: %.2f" % tip, ", meal: %.2f" % total, ", Tol Pay: %.2f" % addTips
    except:
        print "Please input a number~"
        priceCal()

priceCal()

# another way to do that
def priceCal(tax = .06, tipRate = .10):

    cost = raw_input("How much is the meal you ordered: $ ")
    try:
        cost = float(cost)
        tax *= cost
        total = cost + tax
        tip = total * tipRate
        pay = total + tip
        print "Tax: %.2f" % tax, "\nTip: %.2f" % tip, "\nTol Pay: %.2f" % pay
    except:
        print "Please input a number~"
        priceCal()

priceCal()

# yet another way
def priceCal(tax = .06, tipRate = .10):

    cost = raw_input("How much is the meal you ordered: $ ")
    while float(cost) < 0.0:
        cost = raw_input("How much is the meal you ordered: $ ")
    cost = float(cost)
    tax *= cost
    total = cost + tax
    tip = total * tipRate
    pay = total + tip
    return [tax, tip, pay]
get = priceCal()
# if you want to change the tax and tipRate, insert them in the bracelet()upwards.
print "Tax: %.2f" % get[0], "\nTip: %.2f" % get[1], "\nTol Pay: %.2f" % get[2]
