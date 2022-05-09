import json

f = open('learn.json')
DATA = json.load(f)
DATA = DATA['inputdata']
ALL_POSSIBLE_ATTRIBUTES = {}


def getQuantityOfDecisionClasses():
    decisionClasses = {}

    for item in DATA:
        if decisionClasses.get(item[list(item)[-1]]) is None:
            decisionClasses[item[list(item)[-1]]] = 0

    return len(list(decisionClasses))

