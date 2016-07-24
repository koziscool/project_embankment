
from math import sqrt
from math import floor
from copy import copy

letterValues = {  'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
                            'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
                            'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }

factorialDigits = { 0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 
                                7:5040, 8:40320, 9:362880}

def factorial(n): return reduce(lambda x,y:x*y, [1]+range(1,n+1))

def factorialDigitSum( num ):
    return sum([factorialDigits[int(d)] for d in str(num)])

def combinations( n, r ):
    return factorial(n) // factorial(r) // factorial(n - r)

def pythagoreanTriplesUpTo( limit ):
    triples = []
    for a in xrange(1, limit + 1):
        for b in xrange(a, limit + 1):
            c = sqrt(a*a + b*b)
            if c == floor(c) and c <= limit:
                triples.append( {'a':a, 'b':b, 'c':int(c), 'p': a+b+int(c) } ) 
    return triples

def isPal( input ):
    strInput = str( input )
    strLen = len( strInput )
    retVal = True;
    for i in range( strLen // 2 ):
        retVal = ( retVal and strInput[i] == strInput[strLen - i - 1] )

    return retVal

def binaryString( num ):
    if num == 0: return '0'
    if num == 1: return '1'
    return binaryString( num // 2 ) + str( num % 2 )

def digitsDict( num ):
    dict = {}
    for c in str(num):
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
            
    return dict

def factorize( num, primes ):
    factors = []
    primesCopy = copy(primes)
    currentQuotient = num
    while currentQuotient > 1:
        # print currentQuotient, primesCopy
        p = primesCopy.pop(0)
        while currentQuotient % p == 0:
            currentQuotient /= p
            factors.append(p)

    return factors

def factorDictionary( num, primes ):
    factors = factorize( num, primes )
    factorsDict = {}
    for f in factors:
        if factorsDict.get( f ):
            factorsDict[f] += 1
        else:
            factorsDict[f] = 1
    return factorsDict

def incrementNewDict( newDict, factorsDict ):
    for f in factorsDict:
        if newDict[f] < factorsDict[f]:
            newDict[f] += 1
            factorDictSearchIndex = 0
            for f2 in factorsDict:
                if f2 < f:
                    newDict[f2] = 0
            break
    return newDict


def distinctFactors( num, primes ):
    factorsDict = factorDictionary( num, primes )
    newDict = {}
    retArray = []
    for f in factorsDict:
        newDict[f] = 0

    while True:
        product = 1
        for p in newDict:
            product *= p ** newDict[p]
        retArray.append(product)
        if newDict == factorsDict:
            break
        incrementNewDict(newDict, factorsDict)
    return retArray


def numDistinctFactors( num, primes ):
    factorsDict = factorDictionary( num, primes )
    retVal = 1
    for f in factorsDict:
        retVal *= factorsDict[f] + 1
    return retVal

def numDistinctPrimeFactors( num, primes ):
    return len( factorDictionary( num, primes ) )

def totient( num, primes ):
    pDict = factorDictionary(num, primes)
    retVal = num
    for p in pDict:
        retVal = retVal * (p - 1) // p
    return retVal

def sumDivisors( num, primes ):
    factorsDict = factorDictionary( num, primes )
    factorsList = [1]
    for f in factorsDict:
        newList = []
        for item in factorsList:
            for exponent in range(factorsDict[f] + 1):
                newList.append( item * (f ** exponent) )
        factorsList = newList

    sumFactors = reduce( (lambda a, b: a+b), factorsList )
    return sumFactors - num

def leastCommonMultiple( num, primes ):
    lcmFactorDict = {}
    for i in range( 1, num + 1):
        factors = factorize( i, primes )
        priorF = 0
        for f in factors:
            if not f == priorF:
                fcount = 0
            if not lcmFactorDict.get( f ):
                lcmFactorDict[f] = 1
            else:
                fcount += 1
                if fcount > lcmFactorDict[f]:
                    lcmFactorDict[f] = fcount
            priorF = f

    retVal = 1
    for f in lcmFactorDict:
        retVal *= f ** lcmFactorDict[f]

    return retVal

# num any int > 10
def primesUpTo( num ):
    primes = [2, 3, 5, 7]
    for i in xrange( 10, num ):
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break
            if p ** 2 > i:
                break
        if isPrime:
            primes.append( i )

    return primes



