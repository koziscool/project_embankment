
def nextLexPermutation( permutation ):
    permutation = str(permutation)
    pivotValue = permutation[-1]
    endStringSet = set( permutation[-1] )
    
    for i in xrange( len(permutation) - 2 , -1, -1 ):
        # print permutation[i], pivotValue
        if permutation[i] <= pivotValue:
            pivotIndex = i
            break
        endStringSet.add(permutation[i])
        pivotValue = permutation[i] 
    pivotValue = permutation[i] 

    # print pivotIndex, endStringSet, pivotValue
    for c in sorted(endStringSet):
        if c > pivotValue:
            pivotChar = c
            break

    endStringSet.remove(pivotChar)
    endStringSet.add(pivotValue)
    return permutation[0:i] + pivotChar + ''.join(sorted(endStringSet))

def nthPermuatation( num, perm ):
    for i in xrange(num - 1):
        perm = nextLexPermutation(perm)
    return perm

if __name__ == '__main__':
    # print nextLexPermutation( 12453 )
    print nthPermuatation( 1000000, '0123456789' )
