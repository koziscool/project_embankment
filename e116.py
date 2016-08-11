

lengthDic = { 'red':2, 'green':3, 'blue':4 }
minUnkownDic = { 'red':2, 'green':3, 'blue':4 }

solutionsByLength = { }
for i in xrange(-1, lengthDic['red']):
    solutionsByLength[('red', i)] = 1

for i in xrange(-1, lengthDic['green']):
    solutionsByLength[('green', i)] = 1

for i in xrange(-1, lengthDic['blue']):
    solutionsByLength[('blue', i)] = 1


def buildSolutionsUpTo( n, color ):
    if (color, n) in solutionsByLength:
        return solutionsByLength[(color, n)]
    else:
        length = lengthDic[color]
        for i in xrange(minUnkownDic[color], n + 1):
            solutions = solutionsByLength[(color, i-1)] + solutionsByLength[(color, i-length)]
            solutionsByLength[(color, i)] = solutions

    solutionsByLength[(color, 'max')] = i
    return solutionsByLength[(color, n)]

def numCombos(n):
    r = buildSolutionsUpTo(n, 'red')
    g = buildSolutionsUpTo(n, 'green')
    b = buildSolutionsUpTo(n, 'blue')
    # print solutionsByLength
    # print r, g, b
    return r+g+b-3

def e116():
    return numCombos(50)

if __name__ == '__main__':
    print e116()
