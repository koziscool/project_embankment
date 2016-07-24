
regularCal = { 1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7: 31, 8:31, 9:30, 10:31, 11:30, 12: 31 }
leapYearCal = { 1: 31, 2:29, 3:31, 4:30, 5:31, 6:30, 7: 31, 8:31, 9:30, 10:31, 11:30, 12: 31 }

def advanceMonth( year, month, daysFromZero ):
    if year % 4 == 0 and year != 1900:
        daysFromZero += leapYearCal[month + 1]
    else:
        daysFromZero += regularCal[month + 1]

    return daysFromZero     

def numSundaysOnTheFirst(  ):
    numSundays = 0
    daysFromZero = 0
    for year in xrange(1900, 2001):
        for month in xrange(12):
            if year >= 1901 and year <= 2000 and daysFromZero % 7 == 6:
                numSundays += 1
            daysFromZero = advanceMonth( year, month, daysFromZero )

    return numSundays


if __name__ == '__main__':
    print numSundaysOnTheFirst()