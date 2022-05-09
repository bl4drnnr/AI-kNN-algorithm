from parser import getQuantityOfDecisionClasses


def Euklid(learnCase, testCase):
    result = 0

    for key, value in learnCase.items():
        result += (learnCase[key] - testCase[key]) ** 2

    return result ** 0.5

    # return ((learnCase['SL'] - testCase['SL']) ** 2 +
    #         (learnCase['SW'] - testCase['SW']) ** 2 +
    #         (learnCase['PL'] - testCase['PL']) ** 2 +
    #         (learnCase['PW'] - testCase['PW']) ** 2) ** 0.5


def CityBlock(learnCase, testCase):
    result = 0

    for key, value in learnCase.items():
        result += abs(learnCase[key] - testCase[key])

    return result

    # return abs(learnCase['SL'] - testCase['SL']) + \
    #        abs(learnCase['SW'] - testCase['SW']) + \
    #        abs(learnCase['PL'] - testCase['PL']) + \
    #        abs(learnCase['PW'] - testCase['PW'])


def Minkowski(learnCase, testCase):
    result = 0
    q = getQuantityOfDecisionClasses()

    for key, value in learnCase.items():
        result += abs(learnCase[key] - testCase[key]) ** q

    return result ** (1/q)

    # return (abs(learnCase['SL'] - testCase['SL']) ** 3 +
    #         abs(learnCase['SW'] - testCase['SW']) ** 3 +
    #         abs(learnCase['PL'] - testCase['PL']) ** 3 +
    #         abs(learnCase['PW'] - testCase['PW']) ** 3) ** (1 / 3)
