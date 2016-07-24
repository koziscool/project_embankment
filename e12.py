
from math import sqrt

def tri(n):
    return ((n+1)*(n)/2);

def e12():
    for i in range(1,1000000):
        l=[1, tri(i)]
        for j in range(2,int(sqrt(tri(i)))+1):
            if(not tri(i)%j):
                l.append(j)
                l.append(tri(i)/j)

        if(len(l)>500):
            retVal = tri(i)
            break

    return retVal

if __name__ == '__main__':
    print e12()