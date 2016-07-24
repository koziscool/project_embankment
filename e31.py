
coinsList = [
  1, 2, 5, 10, 20, 50, 100, 200 
]

def makeChange( total, coins = coinsList ):
    if total == 1 or total == 0:
        return 1

    bigCoinSize = coins[-1]
    if bigCoinSize == 1:
        return 1
    
    retVal = 0
    numBigCoin = total // bigCoinSize
    newCoins = coins[0:-1];

    for i in xrange( numBigCoin, -1, -1 ):
        retVal += makeChange(total - i * bigCoinSize, newCoins )

    return retVal

print makeChange(200)