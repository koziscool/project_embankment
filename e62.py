


def digits_tuple( n ):
    base_tuple_list = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    for c in str( n ):
        base_tuple_list[ int(c) ] += 1

    return tuple( base_tuple_list )

def e62():
    digits_dict = {}
    for i in xrange( 1, 100000 ):
        i_cube_tuple = digits_tuple( i * i * i )
        if i_cube_tuple in digits_dict:
            digits_dict[i_cube_tuple].append( i )
        else:
            digits_dict[i_cube_tuple] = [ i ]

    min_base = 99999999999999
    for key, val_list in digits_dict.items():
        if len( val_list ) == 5:
            if min( val_list ) < min_base:
                min_base = min( val_list )

    return pow( min_base, 3 )





if __name__ == '__main__':
    print e62(  )
