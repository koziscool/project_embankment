
from math import floor

laminae_type_dict = {}

def get_laminae():
    num_laminae = 0
    for laminae_size in xrange(4 , 10**6+ 1, 4):
        num_laminae_size_n = 0
        for laminae_width in xrange( 1, laminae_size / 4 ):
            k = (laminae_size / float(4 * laminae_width )) - laminae_width
            if k < 0:
                break
            if k > 0 and floor(k) == k:
                num_laminae_size_n += 1
                num_laminae += 1 

        laminae_type_dict[laminae_size] = num_laminae_size_n
    return num_laminae

def aggregate_by_type( limit ):
    aggregate_sum = 0
    for i in xrange(1, limit + 1):
        num_i = [k for k in laminae_type_dict.keys() if laminae_type_dict[k] == i ]
        aggregate_sum += len( num_i )
        # print i, num_i
    return aggregate_sum


def e174():
    get_laminae()
    # print laminae_type_dict
    print aggregate_by_type( 10 )


if __name__ == '__main__':
    print e174()
