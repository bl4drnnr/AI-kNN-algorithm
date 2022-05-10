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
    results = []

    for record in records:
        if results.append(record[KEY_ATTRIBUTE]) not in results:
            results.append(record[KEY_ATTRIBUTE])

    return results


def distanceSumElection(records):
    typesOfDecisions = {}

    for record in records:
        if typesOfDecisions.get(record[KEY_ATTRIBUTE]) is None:
            typesOfDecisions[record[KEY_ATTRIBUTE]] = [float(record['CB'])]
        else:
            typesOfDecisions[record[KEY_ATTRIBUTE]].append(float(record['CB']))

    for key, value in typesOfDecisions.items():
        print(key, value)
    return


def sumOfReciprocalOfTheSquaresOfDistances(records):
    return


def printResult(typeOfResult, data):
    print("Type of metric: " + typeOfResult)
    for item, value in data.items():
        print('Election method: ' + item)
        for x, res in enumerate(value):

            if x == 0:
                print('------------------')
                print('|1\t\t3\t\t5|')
                print('------------------')

            resultString = ""

            for y, rec in enumerate(res):
                if y == 0:
                    resultString += "|" + str(rec) + "\t\t"
                elif y == len(res) - 1:
                    resultString += str(rec) + "|"
                else:
                    resultString += str(rec) + "\t\t"

            print(resultString)

            if x == len(data) - 1:
                print('------------------')
