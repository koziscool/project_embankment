
from utils import primesUpTo

primes = primesUpTo(1000000)

def rotateDigits(num):
    if num < 10:
        return num
    return num % 10 * (10 ** len(str(num / 10)) ) + num / 10 


def circularPrimes():
    retArray = []
    for p in primes:
        if p > 10 and ('0' in str(p) or '2' in str(p) or '4' in str(p) or '5' in str(p) or \
            '6' in str(p) or '8' in str(p)):
            continue
        isCircularPrime = True
        rotatedPrime = rotateDigits( p )
        while rotatedPrime != p:
            if rotatedPrime not in primes:
                isCircularPrime = False
            rotatedPrime = rotateDigits( rotatedPrime )
        if isCircularPrime:
            retArray.append(p)
    return retArray

if __name__ == '__main__':
    print len( circularPrimes() )