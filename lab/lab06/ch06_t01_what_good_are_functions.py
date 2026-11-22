def tax(bill):
    bill *= 1.08
    print("With tax: %f" % bill)

def tip(bill):
    bill *= 1.15
    print("With tip: %f" % bill)

tax(100)
tip(100)
