
def squareDiff( num ):
    sumSquares = 0
    summ = 0
    for i in range(1, num + 1):
        sumSquares += i ** 2
        summ += i

    squaredSum = summ ** 2

    return squaredSum - sumSquares

if __name__ == '__main__':
    print squareDiff( 100 )
