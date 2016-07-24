
numLetters = {  0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
                            11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6,
                            30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:10,
                            200:10, 300:12, 400:11, 500:11, 600:10, 700:12, 800:12, 900:11, 1000:11 }

def numberWordLength( num ):
    if num in numLetters:
        return numLetters[num]

    if num >= 100:
        huns = num / 100
        hunRem = num % 100
        return numberWordLength( huns * 100 ) + 3 + numberWordLength( hunRem )

    ones = num % 10
    tens = num / 10 % 10

    return numberWordLength( tens * 10 ) + numberWordLength( ones )

def numberWordSum( num ):
    return sum( [numberWordLength(i) for i in xrange(1, num + 1)]  )

if __name__ == '__main__':
    print numberWordSum( 1000 )

