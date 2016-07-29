
END_RANGE = 10**9
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def generalized_hamming_numbers( set_in, p ):
    s = set()
    for elt in set_in:
        current = elt
        while current <END_RANGE:
            s.add( current)
            current *= p
    return s

def e204(): 
    s= set([1])
    for p in primes:
        s = generalized_hamming_numbers( s, p )
    return len(s)


if __name__ == '__main__':
    print e204()
