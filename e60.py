
END_RANGE = 10**8

primes = []
primes_digit_length = {}
import time

from math import sqrt

start = time.time()

def totients_up_to( num ):
    totients = [1 for i in xrange(num + 1)]
    for i in xrange(2, num + 1):
        if totients[i] == 1:
            primes.append(i)
            for j in xrange(i, num + 1, i):
                totients[j] *= i - 1
                k = j / i
                while k % i == 0:
                    totients[j] *= i
                    k /= i

totients_up_to( int( sqrt(END_RANGE)) )

def is_prime( num ):
    ret_val = True;
    for p in primes:
        if num % p == 0:
            ret_val = False
            break
        if p * p > num:
            break

    return ret_val

def concat_num( m, n ):
    return int( str(m) +str(n) )

def test_for_concat( p1, p2 ):
    return is_prime( concat_num( p1, p2 ) ) and is_prime( concat_num( p2, p1 ))


def e60():

    pairwise_concat_primes = []
    prime_pair_dict = { }


    for prime_1 in primes:
        for prime_2 in primes:
            if (prime_1 < prime_2 and 
                is_prime( concat_num(prime_1, prime_2) )and 
                is_prime( concat_num(prime_2, prime_1) ) ):
                    pairwise_concat_primes.append( (prime_1, prime_2) )
                    if not prime_1 in prime_pair_dict.keys():
                        prime_pair_dict[prime_1] = [   (prime_1, prime_2) ]
                    else:
                        prime_pair_dict[prime_1].append( (prime_1, prime_2) )

    pairwise_prime_triples = set()

    for key, pair_list in prime_pair_dict.items():
        for p_pair1 in pair_list:
            for p_pair2 in pair_list:
                if p_pair1[1] < p_pair2[1] and test_for_concat(p_pair1[1], p_pair2[1]):
                    pairwise_prime_triples.add(  (p_pair1[0], p_pair1[1], p_pair2[1])  )

    pairwise_prime_quad = set()

    for p_trip1 in pairwise_prime_triples:
        for p_trip2 in pairwise_prime_triples:
            if (p_trip1[0] == p_trip2[0] and 
                p_trip1[1] == p_trip2[1] and 
                p_trip1[2] < p_trip2[2] and 
                test_for_concat(p_trip1[2], p_trip2[2] )  ):

                pairwise_prime_quad.add(  (p_trip1[0], p_trip1[1], p_trip1[2], p_trip2[2])  )


    pairwise_prime_five = set()

    for p_quad1 in pairwise_prime_quad:
        for p_quad2 in pairwise_prime_quad:
            if (p_quad1[0] == p_quad2[0] and 
                p_quad1[1] == p_quad2[1] and 
                p_quad1[2] == p_quad2[2] and 
                (p_quad1[3], p_quad2[3]) in pairwise_concat_primes ):

                pairwise_prime_five.add(  (p_quad1[0], p_quad1[1], p_quad1[2], p_quad1[3], p_quad2[3])  )

    min_five = 99999999999999
    for five in pairwise_prime_five:
        if sum(five) < min_five:
            min_five = sum(five)

    return min_five

if __name__ == '__main__':
    print e60()

