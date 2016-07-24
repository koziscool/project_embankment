
import sys

blank_dict = {}
solutions_dict = {}

def triples_less_than_nine():
    retArr = []
    for i in xrange(0, 10):
        for j in xrange(0, 10):
            for k in xrange(0, 10):
                if i+j+k < 10:
                    retArr.append( (i, j, k) )
    return retArr

trips = triples_less_than_nine()

def init_dict():
    for t in trips:
        blank_dict[t] = 0

    solutions_dict[3] = dict( blank_dict )

    for t in trips:
        if t[0] != 0:
            solutions_dict[3][t] = 1
    return 

init_dict()

def solution_numbers_of_length( n ):
    for i in xrange(4, n+1):
        solutions_dict[i] = dict( blank_dict )
        for c in solutions_dict[i-1]:
            for t in trips:
                if c[-2] == t[0] and c[-1] == t[1]:
                    solutions_dict[i][t] +=  solutions_dict[i-1][c]

def e164():
    NUM_DIGITS = 20
    solution_numbers_of_length( NUM_DIGITS )
    return sum( solutions_dict[NUM_DIGITS].itervalues() )

if __name__ == '__main__':
    print e164()




