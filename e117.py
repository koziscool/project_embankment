

lengthDic = { 'red':2, 'green':3, 'blue':4 }
MIN_UNKNOWN = 2

solutionsByLength = { }
for i in xrange(-10, lengthDic['red']):
    solutionsByLength[i] = 1


def buildSolutionsUpTo( n ):
    if n in solutionsByLength:
        return solutionsByLength[n]
    else:
        for i in xrange(MIN_UNKNOWN, n + 1):
            solutions = solutionsByLength[i-1] + \
                solutionsByLength[ i-lengthDic['red'] ]
            if i >= lengthDic['green']:
                solutions += solutionsByLength[ i-lengthDic['green'] ]
            if i >= lengthDic['blue']:
                solutions += solutionsByLength[ i-lengthDic['blue'] ]
            
            solutionsByLength[i] = solutions

    solutionsByLength['max'] = i
    return solutionsByLength[n]

def numCombos(n):
    return buildSolutionsUpTo(n)


def e117():
    return numCombos(50)

if __name__ == '__main__':
    print e117()
