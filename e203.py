

distinctSquarefreeElements = set()

squares = set()
for i in xrange(2, 100):
    squares.add(i**2)

def checkSquareFactors(n):
    for sq in squares:
        if n % sq == 0:
            return True

    return False

def squarefreeElementsInRowNPascalsTriangle( n ):
    totalInRow = 0
    nFactorial = 1
    for i in xrange(1, n+1):
        nFactorial *= i

    for i in xrange(n+1):
        iFactorial = 1
        for j in xrange(1, i+1):
            iFactorial *= j

        nMinusIFactorial = 1
        for j in xrange(1, n-i+1):
            nMinusIFactorial *= j

        element = nFactorial/iFactorial/nMinusIFactorial

        if not checkSquareFactors(element) and element not in distinctSquarefreeElements:
            totalInRow += element
            distinctSquarefreeElements.add(element)

    return totalInRow



def e203():
    total = 0
    for i in xrange(51):
        total += squarefreeElementsInRowNPascalsTriangle(i)

    return total

if __name__ == '__main__':
    print e203()
