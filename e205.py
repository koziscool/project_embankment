
from random import random
from math import floor

def pyramidDieRoll():
    return int(floor(4*random())) + 1

def petesRoll():
    numDice, retVal = 9, 0
    for i in xrange(numDice):
        retVal += pyramidDieRoll()
    return retVal

def pyramidDieDistribution():
    distribution = {}
    dieSides = 4
    for i in xrange(1, dieSides + 1):
        distribution[i] = 1 / float(dieSides)

    return distribution  

def petesDistribution():
    oldDistribution, newDistribution = pyramidDieDistribution(), {}
    pDistribution = pyramidDieDistribution()
    numRolls = 9

    for i in xrange(numRolls - 1):
        for pk in pDistribution:
            for ok in oldDistribution:
                if pk + ok in newDistribution:
                    newDistribution[pk + ok] += pDistribution[pk] * oldDistribution[ok]
                else:
                    newDistribution[pk + ok] = pDistribution[pk] * oldDistribution[ok]
        oldDistribution = newDistribution
        newDistribution = {}

    return oldDistribution


def cubeDieRoll():
    return int(floor(6*random())) + 1

def colinsRoll():
    numDice, retVal = 6, 0
    for i in xrange(numDice):
        retVal += cubeDieRoll()
    return retVal

def cubeDieDistribution():
    distribution = {}
    dieSides = 6
    for i in xrange(1, dieSides + 1):
        distribution[i] = 1 / float(dieSides)

    return distribution  

def colinsDistribution():
    oldDistribution, newDistribution = cubeDieDistribution(), {}
    cDistribution = cubeDieDistribution()
    numRolls = 6

    for i in xrange(numRolls - 1):
        for pk in cDistribution:
            for ok in oldDistribution:
                if pk + ok in newDistribution:
                    newDistribution[pk + ok] += cDistribution[pk] * oldDistribution[ok]
                else:
                    newDistribution[pk + ok] = cDistribution[pk] * oldDistribution[ok]
        oldDistribution = newDistribution
        newDistribution = {}

    return oldDistribution

def petesProbability():
    pDistribution = petesDistribution()
    cDistribution = colinsDistribution()

    pProbability = 0

    for pk in pDistribution:
        for ck in cDistribution:
            if pk > ck:
                pProbability += pDistribution[pk] * cDistribution[ck]

    return pProbability

def e205():
    return petesProbability()

if __name__ == '__main__':
    print e205()
