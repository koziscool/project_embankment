
collatzLengthDict = { 1:1, 2:2, 4:3 }
collatzMaxLength = 1

def collatzLength( num ):
    if num in collatzLengthDict:
        return collatzLengthDict[num]

    if num % 2 == 0:
        collatzLengthDict[num] = 1 + collatzLength( num // 2 )
        return collatzLengthDict[num]
    else:
        collatzLengthDict[num] = 1 + collatzLength( 3 * num + 1 )
        return collatzLengthDict[num]

if __name__ == '__main__':
    for i in xrange(1, 1000000):
        collatzLength( i )
        if collatzLengthDict[i] > collatzMaxLength:
            longestStartingNumber = i
            collatzMaxLength = collatzLengthDict[i]

    print longestStartingNumber
