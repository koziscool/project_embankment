

import operator

END_RANGE = 120000
primes = []
prime_factor_dict = {}
rad_dict = {}
reverse_rad_dict = {}


def totients_up_to( num ):
    totients = [1 for i in xrange(num + 1)]
    for i in xrange(1, num + 1):
        prime_factor_dict[i] = set()

    for i in xrange(2, num + 1):
        if totients[i] == 1:
            primes.append( i )
            for j in xrange(i, num + 1, i):
                prime_factor_dict[j].add( i )
                totients[j] *= i - 1
                k = j / i
                while k % i == 0:
                    totients[j] *= i
                    k /= i

    return totients


def build_radicals( limit ):
    rad_dict[1] = 1
    reverse_rad_dict[1] = [1]

    for i in xrange( 2, limit + 1):
        reverse_rad_dict[i] = []

    for n in xrange( 2, limit + 1):
        rad = reduce( lambda x, y: x*y, prime_factor_dict[n] )
        rad_dict[n] = rad
        reverse_rad_dict[rad].append( n )


def abc(  limit ):
    counter = 0
    total_c = 0
    for c in xrange(3, limit + 1):
        rad_a = 1
        while rad_a * rad_dict[c] < c: 

            for a in reverse_rad_dict[ rad_a ]:
                b = c - a
                if b <= a:
                    break
                if ( len( prime_factor_dict[a].union(prime_factor_dict[b]) ) ==
                        len( prime_factor_dict[a]) + len(prime_factor_dict[b])
                        and rad_dict[a] * rad_dict[b] * rad_dict[c] < c ):                

                    counter += 1
                    total_c += c

            rad_a += 1

    return total_c

def e127():
    totients_up_to( END_RANGE )
    build_radicals( END_RANGE )
    return abc( END_RANGE )


if __name__ == '__main__':
    print e127()

