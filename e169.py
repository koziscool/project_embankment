
from utils import binaryString

memoPowers2 = {}

def powersOf2(n, digitIndex = None):

    if (n, digitIndex) in memoPowers2:
        # print n, 2**digitIndex, 'i'
        return memoPowers2[(n, digitIndex)]

    if n == 0 or n ==1:
        # print n, 2**digitIndex, 'h'
        return 1

    if digitIndex == None:
        digitIndex = (len(binaryString(n))) - 1

    # print n, 2**digitIndex

    if n == 2**(digitIndex):
        # print n, 2**digitIndex, 'e'
        memoPowers2[(n, digitIndex)] = digitIndex + 1
        return digitIndex + 1
    if n == 2**(digitIndex+1):
        # print n, 2**digitIndex, 'g'
        memoPowers2[(n, digitIndex)] = digitIndex + 1
        return digitIndex+1
    if ( 2** digitIndex ) >= n:
        # print n, 2**digitIndex, 'a'
        retVal = powersOf2(n, digitIndex - 1)
        memoPowers2[(n, digitIndex)] = retVal
        return retVal
    if ( 2** (digitIndex+1) ) == n+1:
        # print n, 2**digitIndex, 'c'
        memoPowers2[(n, digitIndex)] = 1
        return 1
    if (2** (digitIndex+2) - 2 ) < n:
        # print n, 2**digitIndex, 'f'
        memoPowers2[(n, digitIndex)] = 0
        return 0
    if ( 2** (digitIndex+1) ) >= n:
        # print n, 2**digitIndex, 'b'
        retVal = powersOf2(n, digitIndex - 1) + \
            powersOf2(n - 2**digitIndex, digitIndex - 1)
        memoPowers2[(n, digitIndex)] = retVal
        return retVal
    if ( 2** (digitIndex+1) ) <= n-1:
        # print n, 2**digitIndex, 'd'
        retVal = powersOf2(n - 2**digitIndex, digitIndex - 1) + \
            powersOf2(n - 2**(digitIndex+1), digitIndex - 1)
        memoPowers2[(n, digitIndex)] = retVal
        return retVal



if __name__ == '__main__':
    print powersOf2(10**25)
    # print powersOf2(5, 1)

