
from math import floor

def get_laminae():
    num_laminae = 0
    for laminae_size in xrange(4 , 10**6+ 1, 4):
        for laminae_width in xrange( 1, laminae_size / 4 ):
            k = (laminae_size / float(4 * laminae_width )) - laminae_width
            if k < 0:
                break
            if k > 0 and floor(k) == k:
                num_laminae +=1 
                

    return num_laminae

def e173():
    print get_laminae()

if __name__ == '__main__':
    print e173()
