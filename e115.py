

MIN_BLOCK_LENGTH = 50

solutionsByLength = { }
for i in xrange(-1, MIN_BLOCK_LENGTH):
    solutionsByLength[i] = 1

MIN_UNKNOWN = MIN_BLOCK_LENGTH

def buildSolutionsUpTo( n ):
    if n in solutionsByLength:
        return solutionsByLength[n]
    else:
        for i in xrange(MIN_UNKNOWN, n + 1):
            solutions = solutionsByLength[i-1]
            for j in xrange(MIN_BLOCK_LENGTH, i+1):
                solutions += solutionsByLength[i-j-1]
            solutionsByLength[i] = solutions

    solutionsByLength['max'] = i
    return solutionsByLength[n]


def numCombos(n):
    return buildSolutionsUpTo(n)

def numCombosFirstOver(n):
    guess = 100
    beginSearch = 1
    buildSolutionsUpTo(guess)
    while solutionsByLength[solutionsByLength['max']] < n:
        beginSearch = solutionsByLength['max']
        buildSolutionsUpTo( 2*solutionsByLength['max'] )

    while solutionsByLength[beginSearch] < n:
        beginSearch += 1
    return beginSearch



def e114():
    return numCombosFirstOver(1000000)

if __name__ == '__main__':
    print e114()
