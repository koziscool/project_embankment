

END_RANGE = 4 * 10**7

totients = [1 for i in xrange(END_RANGE + 1)]

def totients_up_to( limit ):
    for i in xrange(2, limit + 1):
        if totients[i] == 1:
            for j in xrange(i, limit + 1, i):
                totients[j] *= i - 1
                k = j / i
                while k % i == 0:
                    totients[j] *= i
                    k /= i


totients_up_to( END_RANGE )

totient_chain_length = { 1: 1 }

def build_totient_chain_length( limit ):
    for i in xrange(2, limit + 1):
        totient_chain_length[i] = totient_chain_length[ totients[i] ] + 1

build_totient_chain_length( END_RANGE)

def get_totient_chain_length( num ):
    total = 0
    for key, value in totient_chain_length.items():
        if value == num and totients[key] == key - 1:
            total += key
    return total


def e72():
    return get_totient_chain_length( 25 )

if __name__ == '__main__':
    print e72()

