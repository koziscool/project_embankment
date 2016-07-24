
digitObject = { '1': True, '2': True, '3': True, '4': True, '5': True, '6':True, '7': True, '8': True, '9': True}

def pandigitalProducts():
    pandigitalProductArray = []
    for i in xrange(10, 100):
        for j in xrange(100, 1000):
            productDigits = {}
            if len(str(i*j)) == 4:
                for c in str(i):
                    productDigits[c] = True
                for c in str(j):
                    productDigits[c] = True
                for c in str(i*j):
                    productDigits[c] = True
                if cmp(digitObject, productDigits) == 0:
                    if i*j not in pandigitalProductArray:
                        pandigitalProductArray.append(i*j)

    for i in xrange(1, 10):
        for j in xrange(1000, 10000):
            productDigits = {}
            if len(str(i*j)) == 4:
                for c in str(i):
                    productDigits[c] = True
                for c in str(j):
                    productDigits[c] = True
                for c in str(i*j):
                    productDigits[c] = True
                if cmp(digitObject, productDigits) == 0:
                    if i*j not in pandigitalProductArray:
                        pandigitalProductArray.append(i*j)

    return pandigitalProductArray

if __name__ == '__main__':
    print sum( pandigitalProducts() )
