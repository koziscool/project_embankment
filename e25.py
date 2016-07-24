
def fiboWithDigits( digits ):
    fibo = [ 1, 2 ]
    while len( str(fibo[-1] )) < digits:
        fibo.append( fibo[-1] + fibo[-2] )
    
    return len( fibo ) + 1


if __name__ == '__main__':
    print fiboWithDigits( 1000 )
    
