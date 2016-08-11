

MIN_BLOCK_LENGTH = 3
MIN_UNKNOWN = 4

solutionsByLength = { 3:2, 2:1, 1:1, 0:1, -1:1 }

def buildSolutionsUpTo( n ):
    if n in solutionsByLength:
        return solutionsByLength[n]
    else:
        for i in xrange(MIN_UNKNOWN, n + 1):
            solutions = solutionsByLength[i-1]
            for j in xrange(MIN_BLOCK_LENGTH, i+1):
                solutions += solutionsByLength[i-j-1]
            solutionsByLength[i] = solutions

    return solutionsByLength[n]

def numCombos(n):
    return buildSolutionsUpTo(n)

def e114():
    return numCombos(50)

if __name__ == '__main__':
    print e114()
