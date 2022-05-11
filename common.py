from parser import getQuantityOfDecisionClasses, getKeyAttribute

KEY_ATTRIBUTE = getKeyAttribute()
TYPES_OF_METRICS = ['EU', 'CB', 'M3']


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
    if len(resultsSet) == 1 and testRecord[KEY_ATTRIBUTE] == records[0][KEY_ATTRIBUTE]:
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
    typesOfDecisions = extractTypesIfDecisions(records, metric)

    if len(list(typesOfDecisions)) == 1 and testRecord[KEY_ATTRIBUTE] == records[0][KEY_ATTRIBUTE]:
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

        minDistances = {'minDistances': [], 'minDistance': None, 'minDistanceClass': None}

        for key, value in typesOfDecisions.items():
            if typesOfDecisions.get(str(key) + "_aver") is not None:
                minDistances['minDistances'].append(abs(typesOfDecisions['average'] - typesOfDecisions[str(key) + "_aver"]))

        minDistances['minDistance'] = min(minDistances['minDistances'])

        for key, value in typesOfDecisions.items():
            if typesOfDecisions.get(str(key) + "_aver") is not None:
                if abs(typesOfDecisions['average'] - typesOfDecisions[str(key) + "_aver"]) == minDistances['minDistance']:
                    minDistances['minDistanceClass'] = str(key)

        if testRecord[KEY_ATTRIBUTE] == minDistances['minDistanceClass']:
            return True
        else:
            return False


def sumOfReciprocalOfTheSquaresOfDistances(records, testRecord, metric):
    typesOfDecisions = extractTypesIfDecisions(records, metric)

    if len(list(typesOfDecisions)) == 1 and testRecord[KEY_ATTRIBUTE] == records[0][KEY_ATTRIBUTE]:
        return True
    else:
        tempTypesOfDecisions = {}
        sumOfAll = 0

        for key, value in typesOfDecisions.items():
            for val in value:
                sumOfAll += 1/(val ** 2)
                if tempTypesOfDecisions.get(str(key) + "_sq") is None:
                    tempTypesOfDecisions[str(key) + "_sq"] = 1/(val ** 2)
                else:
                    tempTypesOfDecisions[str(key) + "_sq"] += 1/(val ** 2)

        for key, value in tempTypesOfDecisions.items():
            typesOfDecisions[key] = value

        typesOfDecisions['sumOfAll'] = sumOfAll

        minDistances = {'minDistances': [], 'minDistance': None, 'minDistanceClass': None}

        for key, value in typesOfDecisions.items():
            if typesOfDecisions.get(str(key) + "_sq") is not None:
                minDistances['minDistances'].append(abs(typesOfDecisions['sumOfAll'] - typesOfDecisions[str(key) + "_sq"]))

        minDistances['minDistance'] = min(minDistances['minDistances'])

        for key, value in typesOfDecisions.items():
            if typesOfDecisions.get(str(key) + "_sq") is not None:
                if abs(typesOfDecisions['sumOfAll'] - typesOfDecisions[str(key) + "_sq"]) == minDistances['minDistance']:
                    minDistances['minDistanceClass'] = str(key)

        if testRecord[KEY_ATTRIBUTE] == minDistances['minDistanceClass']:
            return True
        else:
            return False


def extractTypesIfDecisions(records, metric):
    typesOfDecisions = {}

    for record in records:
        if typesOfDecisions.get(record[KEY_ATTRIBUTE]) is None:
            typesOfDecisions[record[KEY_ATTRIBUTE]] = [float(record[metric])]
        else:
            typesOfDecisions[record[KEY_ATTRIBUTE]].append(float(record[metric]))

    return typesOfDecisions


def getMethodName(name):
    return {
        'normalElection': 'Normal elections',
        'distanceSumElection': 'Summary distance elections',
        'sumOfReciprocal': 'Summary of reciprocal'
    }.get(name)


def printResult(typeOfResult, data):
    print("Type of metric: " + typeOfResult)
    for item, value in data.items():
        print('Election method: ' + getMethodName(item))
        t = []
        for x in value:
            t.append(x)
            if len(t) == 3:
                print(t)
                t = []
        print('---------------')
    print('###############################')
