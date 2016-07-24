
from utils import primesUpTo

primes = primesUpTo( 2000000 )
theSum = reduce( (lambda x, y: x+y), primes )

if __name__ == '__main__':
    print theSum
