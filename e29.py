
def numDistinctPowers( begin, end ): 
    powers = []
    for j in xrange(begin, end + 1):
        powers.append( [ j ** i for i in xrange(begin, end + 1) ] )

    powersDict = {}

    for p in powers:
        for num in p:
            powersDict[num] = True

    return len(powersDict)

if __name__ == '__main__':
    print numDistinctPowers(2, 100)

