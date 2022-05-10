from parser import getQuantityOfDecisionClasses, getKeyAttribute

KEY_ATTRIBUTE = getKeyAttribute()


def Euklid(learnCase, testCase):
    result = 0

    for key, value in learnCase.items():
        if key != KEY_ATTRIBUTE:
            result += (learnCase[key] - testCase[key]) ** 2

    return format(result ** 0.5, ".3f")


def CityBlock(learnCase, testCase):
    result = 0

    for key, value in learnCase.items():
        if key != KEY_ATTRIBUTE:
            result += abs(learnCase[key] - testCase[key])

    return format(result, ".3f")


def Minkowski(learnCase, testCase):
    result = 0
    q = getQuantityOfDecisionClasses()

    for key, value in learnCase.items():
        if key != KEY_ATTRIBUTE:
            result += abs(learnCase[key] - testCase[key]) ** q

    return format(result ** (1/q), ".3f")


def normalElection(records):
    return


def distanceSumElection(records):
    return


def sumOfReciprocalOfTheSquaresOfDistances(records):
    return


def printResult(typeOfResult, data):
    return
