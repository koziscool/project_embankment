
strBigBinary = str( 2 ** 1000)

digitTotal = 0

for c in strBigBinary:
    digitTotal += int(c)

if __name__ == '__main__':
    print digitTotal