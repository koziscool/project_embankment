
from utils import pythagoreanTriplesUpTo

def pythagoreanPerimiter( num ):
    triples = pythagoreanTriplesUpTo( num )
    perimeterTriples = filter( lambda t: t['p'] == num, triples) 
    return perimeterTriples

if __name__ == '__main__':
    triple = pythagoreanPerimiter( 1000 )[0]
    print triple['a'] * triple['b'] * triple['c']