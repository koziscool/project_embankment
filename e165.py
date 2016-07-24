
NUM_NUMBERS = 20000
NUM_SEGMENTS = 5000
bbs = []
segments = []
true_intersection_points = set()

def blum_blum_shub( n ):
    s = 290797
    for i in xrange( n):
        s = (s * s) % 50515093
        t = s % 500
        bbs.append(t)

blum_blum_shub( NUM_NUMBERS )

def create_segments():
    for i in xrange(NUM_SEGMENTS):
        segments.append( (bbs[4*i], bbs[4*i+1], bbs[4*i+2], bbs[4*i+3]) )

create_segments(  )
# print len( segments )

def general_form_of_line( x0, y0, x1, y1):
    l = y0 - y1
    m = x1 - x0
    n = (x0 - x1)*y0 + (y1 - y0)*x0
    return (l, m, n)

def intersection_point( line1, line2 ):
    d = float(line1[1]*line2[0] - line1[0]*line2[1]) 
    # print d
    if d == 0:
        return None

    x = (line1[2]*line2[1] - line1[1]*line2[2]) / d
    y = (line1[0]*line2[2] - line1[2]*line2[0]) / d
    return (x, y)

def is_interior_of_segment( point, segment ):

    if segment[2] == segment[0]:
        t2 = (point[1] - segment[1]) / (segment[3] - segment[1])
        if t2 > 0 and t2 < 1 and point[0] == segment[0]:
            return  True
        else:
            return False

    if segment[3] == segment[1]:
        t1 = (point[0] - segment[0]) / (segment[2] - segment[0])
        if t1 > 0 and t1 < 1 and point[1] == segment[1]:
            return  True
        else:
            return False

    t1 = (point[0] - segment[0]) / (segment[2] - segment[0])
    t2 = (point[1] - segment[1]) / (segment[3] - segment[1])

    if t1 > 0 and t1 < 1:
        return  True
    else:
        return False

def all_true_intersection_points():
    for i in xrange( len(segments) ):
        line1 = general_form_of_line( segments[i][0], segments[i][1],  segments[i][2], segments[i][3] )
        for j in xrange( i+1, len(segments) ):
            line2 = general_form_of_line( segments[j][0], segments[j][1],  segments[j][2], segments[j][3] )
            point = intersection_point( line1, line2 )

            if point and is_interior_of_segment(point, segments[i]) and is_interior_of_segment( point, segments[j] ):
                true_intersection_points.add( point )

def e165():
    all_true_intersection_points()
    return len(true_intersection_points)

if __name__ == '__main__':
    print e165()
