
def evenFibonacci( limit ):
    fibo = [ 1, 2 ]
    while fibo[-1] < limit:
        fibo.append( fibo[-1] + fibo[-2] )
    return reduce ( lambda x, y:  x + y, filter( (lambda x: x%2 == 0 ), fibo ))

if __name__ == '__main__':
    print evenFibonacci( 4000000 )
    