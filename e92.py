
resolvesTo1 = { 1: True }
resolvesTo89 = { 89: True }

def squareDigitSum( num ):
    return sum([ int(c)*int(c) for c in str(num) ])

def squareDigitSumsEndingIn89( limit ):
    for i in range(1, limit):
        thisIteration = i
        while thisIteration not in resolvesTo1 and thisIteration not in resolvesTo89:
            thisIteration = squareDigitSum( thisIteration )
            if thisIteration in resolvesTo1:
                resolvesTo1[i] = True
            if thisIteration in resolvesTo89:
                resolvesTo89[i] = True

    return len( resolvesTo89 )

def e92():
    return squareDigitSumsEndingIn89( 10**8 )

if __name__ == '__main__':
    print e92() 
