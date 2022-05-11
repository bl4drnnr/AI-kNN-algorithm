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


def normalElection(records, testRecord):
    results = []

    for record in records:
        results.append(record[KEY_ATTRIBUTE])

    resultsSet = set(results)

    if len(resultsSet) == 1:
        return True
    else:
        decisionClasses = {}
        checkIfCorrectRecord = False
        maxValue = 0

        for item in results:
            if decisionClasses.get(item) is None:
                decisionClasses[item] = 1
            else:
                decisionClasses[item] += 1
        for key, value in decisionClasses.items():
            if maxValue < value:
                maxValue = value
        for key, value in decisionClasses.items():
            if value == maxValue and key == testRecord[KEY_ATTRIBUTE]:
                checkIfCorrectRecord = True
        if checkIfCorrectRecord:
            return True
        else:
            return False


def distanceSumElection(records, testRecord, metric):
    typesOfDecisions = {}

    for record in records:
        if typesOfDecisions.get(record[KEY_ATTRIBUTE]) is None:
            typesOfDecisions[record[KEY_ATTRIBUTE]] = [float(record[metric])]
        else:
            typesOfDecisions[record[KEY_ATTRIBUTE]].append(float(record[metric]))

    if len(list(typesOfDecisions)) == 1:
        return True
    else:
        # Look for average value
        tempTypesOfDecisions = {}
        average = {'value': 0, 'count': 0}

        for key, value in typesOfDecisions.items():
            for val in value:
                average['value'] += val
                average['count'] += 1
                if tempTypesOfDecisions.get(str(key) + "_aver") is None:
                    tempTypesOfDecisions[str(key) + "_aver"] = val/len(value)
                else:
                    tempTypesOfDecisions[str(key) + "_aver"] += val/len(value)

        typesOfDecisions['average'] = average['value'] / average['count']

        for key, value in tempTypesOfDecisions.items():
            typesOfDecisions[key] = value

        minDistance = 0
        for key, value in typesOfDecisions.items():
            if typesOfDecisions.get(str(key) + "_aver") is not None:
                print(typesOfDecisions['average'] - typesOfDecisions[str(key) + "_aver"])
                if minDistance > abs(typesOfDecisions['average'] - typesOfDecisions[str(key) + "_aver"]):
                    minDistance = format(abs(typesOfDecisions['average'] - typesOfDecisions[str(key) + "_aver"]), ".3f")
        typesOfDecisions['minDistance'] = minDistance
        print(typesOfDecisions)
    return False


def sumOfReciprocalOfTheSquaresOfDistances(records, testRecord):
    return


def printResult(typeOfResult, data):
    print("Type of metric: " + typeOfResult)
    for item, value in data.items():
        print('Election method: ' + item)
        t = []
        for x in value:
            t.append(x)
            if len(t) == 3:
                print(t)
                t = []
        print('---------------')
    print('###############################')
