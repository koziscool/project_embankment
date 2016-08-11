
import operator

primes = []
prime_factor_dict = {}
rad_dict = {}

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
    for n in xrange( 2, limit + 1):
        rad_dict[n] =  reduce( lambda x, y: x*y, prime_factor_dict[n] )

def e124(  ):
    end_range = 100000
    query = 10000
    totients_up_to( end_range )
    build_radicals( end_range )

    sorted_radical_list = sorted(rad_dict.items(), key=operator.itemgetter(1))
    return sorted_radical_list[query - 1][0]
   
if __name__ == '__main__':
    print e124()

