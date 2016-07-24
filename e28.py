
def diagonalNumbersWLayers( num ):
    diagonalNumbers = [ 1, 3, 5, 7, 9 ]
    numLayers = 2
    
    while numLayers < num:
        lastNum = diagonalNumbers[-1]
        delta = 2* ( numLayers )
        for i in xrange(4):
            newNum = lastNum + delta + i*delta
            diagonalNumbers.append( newNum )
        numLayers += 1

    return sum(diagonalNumbers)

if __name__ == '__main__':
    print diagonalNumbersWLayers( 501 )