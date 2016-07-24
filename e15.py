
from utils import combinations

def pascalsRow( num ):
    retVal = []
    for i in range( num +1 ):
        retVal.append( combinations(num, i))
    return retVal

def gridRoutes( num ):
    theRow = pascalsRow(num)
    numRoutes = sum( i*i for i in theRow )
    return numRoutes


if __name__ == '__main__':
    print gridRoutes(20)
    