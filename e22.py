
from utils import letterValues

txt = open('p022_names.txt')
names = txt.read().split(',')
names = [ name.strip('"') for name in names ]
names.sort()

nameValues = [ (i+1) * sum( letterValues[c] for c in names[i] ) for i in xrange(len(names)) ]

if __name__ == '__main__':
    print sum(nameValues)
