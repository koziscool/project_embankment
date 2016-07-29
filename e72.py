

def sumtotientsUpTo( num ):
    totients = [1 for i in xrange(num + 1)]
    for i in xrange(2, num + 1):
        if totients[i] == 1:
            for j in xrange(i, num + 1, i):
                totients[j] *= i - 1
                k = j / i
                while k % i == 0:
                    totients[j] *= i
                    k /= i

    return sum(totients[2:])

def e72():
    return sumtotientsUpTo( 1000000 )    

if __name__ == '__main__':
    print e72()