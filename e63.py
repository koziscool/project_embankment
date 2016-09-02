


def e63():
    counter = 0
    base = 1
    while base < 10:
        exponent = 1
        while True:
            if len( str( pow(base, exponent) )) == exponent:
                # print base, exponent
                counter += 1
            if len( str( pow(base, exponent) )) < exponent:
                break
            exponent += 1
        base += 1

    return counter


if __name__ == '__main__':
    print e63(  )