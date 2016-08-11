
def generalFormOfLineByTwoPoints( x0, y0, x1, y1):
    l = y0 - y1
    m = x1 - x0
    n = (x0 - x1)*y0 + (y1 - y0)*x0
    return (l, m, n)

def polarityOfPointRelativeToLine(x, y, l, m, n):
    return l*x + m*y + n

def sameSideOfLine(x0, y0, x1, y1, l, m, n):
    if polarityOfPointRelativeToLine(x0, y0, l, m, n) * \
        polarityOfPointRelativeToLine(x1, y1, l, m, n) > 0:
            return True
    else:
        return False

def e102():
    txt = open('p102_triangles.txt')
    lines = txt.read().split('\n')
    pointData = [ line.split(',') for line in lines if line != '' ]
    numTrianglesContainingOrigin = 0
    for row in pointData:
        x0, y0 = int(row[0]), int(row[1])
        x1, y1 = int(row[2]), int(row[3])
        x2, y2 = int(row[4]), int(row[5])

        l01, m01, n01 = generalFormOfLineByTwoPoints(x0, y0, x1, y1)
        l02, m02, n02 = generalFormOfLineByTwoPoints(x0, y0, x2, y2)
        l12, m12, n12 = generalFormOfLineByTwoPoints(x1, y1, x2, y2)

        if sameSideOfLine(x0, y0, 0, 0, l12, m12, n12) and \
            sameSideOfLine(x1, y1, 0, 0, l02, m02, n02) and \
            sameSideOfLine(x2, y2, 0, 0, l01, m01, n01):
                numTrianglesContainingOrigin += 1

    return numTrianglesContainingOrigin


if __name__ == '__main__':
    print e102()
