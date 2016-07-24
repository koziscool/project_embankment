
from utils import primesUpTo

primes = primesUpTo( 1000000 )

def nthPrime( num ):
    if len( primes ) >= num:
        return primes[num - 1]

if __name__ == '__main__':
    print nthPrime( 10001 )
