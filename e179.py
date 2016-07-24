
from math import sqrt
primes = [2]

def consecutive_divisors_up_to2( limit ):
    total_consecutive_divisors = 0
    current_num_divisors = 2
    for i in xrange(3,limit+1):
        previous_num_divisors = current_num_divisors
        divisors = set( [1, i] )
        for j in range(2,int(sqrt(i))+1):
                if( not i%j ):
                    divisors.add(j)
                    divisors.add( i/j)
        current_num_divisors = len( divisors )

        if current_num_divisors == previous_num_divisors:
            total_consecutive_divisors += 1

    return total_consecutive_divisors


def consecutive_divisors_up_to(  limit ):
    total_consecutive_divisors = 0
    current_num_divisors = 2
    small_primes = []
    current_prime_index = 0
    current_prime = primes[current_prime_index]
    for i in xrange(3,limit+1):
        previous_num_divisors = current_num_divisors
        divisors = set( [1, i] )
        small_divisors = [1]
        if current_prime**2 <= i:
            current_prime_index += 1
            small_primes.append( current_prime )
            current_prime = primes[current_prime_index]
            

        for p in small_primes:
            for sd in small_divisors:
                test_num = sd * p
                if( not i%test_num ):
                    divisors.add(test_num)
                    small_divisors.append(test_num)
                    divisors.add( i/test_num)

        current_num_divisors = len( divisors )
        if current_num_divisors == 2:
            primes.append( i )
        if current_num_divisors == previous_num_divisors:
            total_consecutive_divisors += 1
            # print i-1, i, current_num_divisors
    return total_consecutive_divisors

def consecutive_divisors_up_to3(  limit ):
    divisors_list = [1] * (limit + 1)
    for i in xrange(2, limit + 1):
        for j in xrange( i, limit+1, i ):
            divisors_list[j] += 1

    total_consecutive_divisors = 0
    for i in xrange(2, limit + 1):
        if divisors_list[i] == divisors_list[i-1]:
            total_consecutive_divisors += 1

    return total_consecutive_divisors

def e179():
    return consecutive_divisors_up_to3( 10**7 )

if __name__ == '__main__':
    print e179()
