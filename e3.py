
from utils import primesUpTo
from utils import factorize

primes = primesUpTo( 1000000 )

def largestPrimeFactor( num ):
    factors = factorize( num, primes )
    return max( factors )

if __name__ == '__main__':
    print largestPrimeFactor( 600851475143 )
