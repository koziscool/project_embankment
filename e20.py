
from utils import factorial

strFac = str( factorial(100) )
digitTotal = 0

for c in strFac:
    digitTotal += int(c)

if __name__ == '__main__':
    print digitTotal