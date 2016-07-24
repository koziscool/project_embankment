
from math import sqrt

perfect = []
abundant = []
deficient = []

def genFactors(n):
    yield 1
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            yield i
            if n / i != i:
                yield n/i
        i += 1
    yield n

def factors2(n):
    return list(genFactors(n))

def sortIntsUpTo( num ):
    for i in xrange(2, num + 1):
        sortOn = sum(factors2(i)) - i
        if sortOn < i:
            deficient.append(i)
        if sortOn > i:
            abundant.append(i)
        if sortOn == i:
            perfect.append(i)

def notAbundantSums():
    retArray = []
    abundantSumSet = set()
    for i in abundant:
        for j in abundant:
           if i+j not in abundantSumSet:
                abundantSumSet.add(i+j)

    for i in xrange(1, 28124):
        if i not in abundantSumSet:
            retArray.append(i)

    return retArray

if __name__ == '__main__':
    sortIntsUpTo( 28123 )
    print sum(notAbundantSums())