
from utils import factorialDigitSum

def curiousNumbers():
    curious = []
    for i in xrange(10, 1000000):
        if factorialDigitSum(i) == i:
            curious.append(i)
    return curious

if __name__ == '__main__':
    print sum( curiousNumbers() )
