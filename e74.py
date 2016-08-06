
factorials = { 0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 
                                7:5040, 8:40320, 9:362880}


END_RANGE  = 10**6
factorial_chain_length = { 1:1, 2:1 }

def factorial_chain( num, current_chain ):
    if num in factorial_chain_length:
        for i in xrange( len(current_chain) - 1 ):
            factorial_chain_length[ current_chain[i] ] = factorial_chain_length[ num ] + len( current_chain ) - i - 1
        return factorial_chain_length[ num ]

    else:
        factorial_digit_sum = sum( [factorials[int(d)] for d in str(num)] )
        if factorial_digit_sum in current_chain:
            index_mark = current_chain.index( factorial_digit_sum )
            repeat_loop = current_chain[ index_mark: ]

            for i in xrange( index_mark ):
                factorial_chain_length[ current_chain[i] ] = len( current_chain ) - i

            for i in xrange( index_mark, len( current_chain) ):
                factorial_chain_length[ current_chain[i] ] = len( repeat_loop )

            return factorial_chain_length[num]

        else:
            new_chain = current_chain + [factorial_digit_sum]
            factorial_chain( factorial_digit_sum, new_chain )
            return factorial_chain_length[num]

def e74():
    for i in xrange(1, END_RANGE):
        factorial_chain( i, [i] )

    total = 0
    for key, val in factorial_chain_length.items():
        if key < 10**6 and val == 60:
            total += 1

    return total


if __name__ == '__main__':
    print e74(  )

