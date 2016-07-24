

def unitFraction(  ):
    maxCycleLength  = 1
    maxCycleIndex = 1
    for i in xrange(2, 1001):
        expansion = []
        currentTuple = (1, 0)
        dividend = 1
        decimal = 0
        while currentTuple not in expansion:
            expansion.append(currentTuple)
            dividend *= 10
            decimal = dividend / i 
            dividend = dividend % i 
            currentTuple = dividend, decimal

        if len(expansion) - expansion.index(currentTuple) > maxCycleLength:
            maxCycleLength = len(expansion) - expansion.index(currentTuple)
            maxCycleIndex = i
    return maxCycleIndex

if __name__ == '__main__':
    print unitFraction()
    