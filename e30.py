

def fifthPowerDigitSums():
    retArray = []
    for i in xrange(10, 1000000 ):
        if i == sum( int(c) ** 5 for c in str(i) ):
            retArray.append(i)

    return retArray

if __name__ == '__main__':
    print sum( fifthPowerDigitSums() )