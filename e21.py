
from utils import sumDivisors
from utils import primesUpTo

def sumAmicableNumbersUpTo( num ):
    primes = primesUpTo( num )
    sumFactorsDict = {}
    amicableList = []

    for i in xrange( 1, num ):
        sumFactorsDict[i] = sumDivisors(i, primes )

    for i in xrange( 2, num ):
        if sumFactorsDict[i] < num and \
        sumFactorsDict[i] != i and \
        sumDivisors( sumFactorsDict[i], primes ) == i:
            amicableList.append( i )

    return  reduce( (lambda a, b: a+b), amicableList )

if __name__ == '__main__':
    print sumAmicableNumbersUpTo ( 10000 )
